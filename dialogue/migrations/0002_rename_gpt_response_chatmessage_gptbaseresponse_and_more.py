# Generated by Django 5.0.4 on 2024-05-05 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dialogue', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatmessage',
            old_name='gpt_response',
            new_name='gptBaseResponse',
        ),
        migrations.RenameField(
            model_name='chatmessage',
            old_name='user_input',
            new_name='gptFinalResponse',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='userInput',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]