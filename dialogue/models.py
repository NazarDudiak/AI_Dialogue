from django.db import models


class ChatMessage(models.Model):
    objects = models.Manager()

    userInput = models.TextField()
    gptBaseResponse = models.TextField()
    gptFinalResponse = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User Input: {self.userInput}"
