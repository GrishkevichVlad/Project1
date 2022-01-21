import telebot

# import json


# Создаем экземпляр бота
bot = telebot.TeleBot('')


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start", "help"])
def start(message):
    bot.reply_to(message, 'Я на связи. Напиши мне что-нибудь')

from fun_json import bot_json


# Получение сообщений от юзера
@bot.message_handler(func=lambda m: True)
def handle_text(message):
    response = bot_json(message.text)
    bot.send_message(message.from_user.id, response)


bot.polling()

