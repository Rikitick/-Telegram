import requests
from translate import Translator
import telebot
import re
import os

def telegram_bot():
    bot = telebot.TeleBot("Your token")

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, f'Приветствую, {message.from_user.first_name}. Я - Геральд.\n Я всегда подскажу актуальный прогноз погоды во всём мире, чтобы ты не замёрз! \nУдачного использования!😉')
        os.getcwd()
        sti = open('Замёрз.png', "rb")
        bot.send_sticker(message.chat.id, sti)
        bot.send_message(message.chat.id, 'Напишите название города...')

    @bot.message_handler()
    def main_sender(message):
        try:
            translator = Translator(from_lang="eu", to_lang="ru")
            req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=05ede9238f3a74ff2ba2364080a5a543&units=metric")
            temp = req.json()
            bot.send_message(message.chat.id, f"На данный момент в городе {message.text} температура воздуха {int(round(temp['main']['temp'], 0))} °C, {translator.translate(temp['weather'][0]['description'])}\nВлажность: {temp['main']['humidity']}%")
        except:
            bot.send_message(message.chat.id, "Хм... Я не знаю такого города   :(")
            bot.send_message(message.chat.id, "Попробуй ещё раз...")

    bot.polling()

if __name__ == "__main__":
    telegram_bot()