# -*- coding: utf-8 -*-
import telebot
from telebot import types
import configloader
import logging
import threading
from datetime import datetime
from messages import *  # Инмпортируем все с файла сообщений



try:
    import coloredlogs
except ImportError:
    coloredlogs = None


def main():
    threading.current_thread().name = "bot"

    # Настройка ведения журнала
    log = logging.getLogger("bot")
    logging.root.setLevel(configloader.config["Logging"]["level"])
    stream_handler = logging.StreamHandler()
    if coloredlogs is None:
        stream_handler.formatter = logging.Formatter(configloader.config["Logging"]["format"], style="{")
    else:
        stream_handler.formatter = coloredlogs.ColoredFormatter(configloader.config["Logging"]["format"], style="{")
    logging.root.handlers.clear()
    logging.root.addHandler(stream_handler)
    log.info("Журнал успешно настроен!")

    # Игнорируйте большинство журналов python-telegram-bot, так как большую часть времени они бесполезны
    logging.getLogger("telegram").setLevel("ERROR")


# Выводим действия пользователей в консоль
def log(message):
    out = ("{0} [{1}], (id: {2} {3}), >> {4}".format(datetime.now(),
                                                     message.chat.id,
                                                     message.from_user.username,
                                                     message.from_user.id,
                                                     message.text))
    print(out)
    datetime.strftime(datetime.now(), '%Y-%m-%d')


bot = telebot.TeleBot(configloader.config["Telegram"]["token"])


@bot.message_handler(commands=['start'])
def send_welcome(message):
#    Вызов клавиатуры и аргументы - уменьшить и скрыть
     keyboard_add = types.ReplyKeyboardMarkup(True, True)
#    Кнопки - можно добавлять до 12шт
     keyboard_add.row('Подать обьявление')
#    keyboard_add = types.KeyboardButton("Подать обьявление")
     bot.send_photo(message.chat.id, 'D:/TelegramBot/TBot_SalonSupport/Photo/massageLOGO.jpg')
     msg = bot.send_message(message.chat.id, WELCOME_MESSAGE, reply_markup=keyboard_add)
     log(message)


if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)