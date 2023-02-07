import openai
import telebot
from telebot import TeleBot

openai.api_key = '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'
bot: TeleBot = telebot.TeleBot("5616289171:AAF-4sX_UrgGvyTxWwBPpbZiR_9NXuPP40E")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, am an AI-powered bot. Ask me a questions and I will do my best to answer it!")


@bot.message_handler(func=lambda _: True)
def handle_message(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.5,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
    )
    bot.send_message(chat_id=message.from_user.id, text=response['choices'][0]['text'])


bot.polling()
