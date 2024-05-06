import os

from django.shortcuts import render
from .forms import ChatForm
from .models import ChatMessage
from openai import OpenAI

from AIChatbox.settings import OPENAI_API_KEY


def chat_view(request):
    gpt_response = None

    if request.method == 'POST':
        form = ChatForm(request.POST)

        if form.is_valid():
            user_input = form.cleaned_data['userInput']
            if len(user_input) == 0:
                error_message = "Please enter something in the input field."
                return render(request, 'dialogue/chat.html', {'form': form, 'error_message': error_message})

            client = OpenAI(api_key=OPENAI_API_KEY)
            base_prompt_template = f"""{user_input}
                        Give me 3 main problems which my product is solving. ONLY 3 PROBLEMS without another information.
                        - show how our product solves problems 
                        - write in simple words 
                        - make paragraphs where it's okay"""

            base_response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": base_prompt_template}],
                temperature=0.8
            )
            gpt_base_response = base_response.choices[0].message.content

            latest_prompt_template = f"""{gpt_base_response}
            Above are the problems that my product solves. Based on them, write 3 advertisements for Facebook.
            Ads CRITERIA:
            1. Brevity and Clarity: Try to formulate your message as concisely and clearly as possible. The ideal text length is about 125-150 characters. This is enough to convey the main idea without overwhelming the reader.
            2. Captivating Beginning: The first few words should grab the audience's attention and interest. It could be a question, a statement, or a curiosity-inducing sentence.
            3. Call to Action (CTA): Include a clear and direct call to action. This could be a call to purchase, learn more, register, etc. It should be clear and easily noticeable.
            4. Benefits and Uniqueness: Highlight the unique benefits of your product or service. Why should people pay attention to this?"""

            latest_response = client.chat.completions.create(
                model="gpt-3.5-turbo-1106",
                messages=[{"role": "user", "content": latest_prompt_template}],
                temperature=0.8
            )
            gpt_latest_response = latest_response.choices[0].message.content

            ChatMessage.objects.create(
                userInput=user_input,
                gptBaseResponse=gpt_base_response,
                gptFinalResponse=gpt_latest_response
            )

            gpt_response = gpt_latest_response
        return render(request, 'dialogue/chat.html', {'form': form, 'gpt_response': gpt_response})
    else:
        form = ChatForm()
        return render(request, 'dialogue/chat.html', {'form': form, 'gpt_response': gpt_response})
