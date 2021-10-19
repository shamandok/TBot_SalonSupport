# -*- coding: utf-8 -*-
import logging
import sys
import threading
from datetime import datetime
import telebot
from telebot import types
import bot_functions as bf
import configloader
from mybot_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE
from telebot.types import ReplyKeyboardRemove, CallbackQuery
import transitions



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
    log.info("Модуль логгирования успешно настроен!")

    # Игнорируйте большинство журналов python-telegram-bot, так как большую часть времени они бесполезны
    logging.getLogger("telegram").setLevel("ERROR")

    # Test the specified token
    log.info("Проверяем токен бота...")
    me = bot.get_me()
    if me is None:
        logging.fatal("The token you have entered in the config file is invalid. Fix it, then restart greed.")
        sys.exit(1)
    log.info("Токен Действителен!")
    log.info(f"@{me.username} Запущен!")


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


user_data = {}

# Creates a unique calendar
calendar = Calendar(language=RUSSIAN_LANGUAGE)
calendar_1_callback = CallbackData("calendar_1", "action", "year", "month", "day")


@bot.message_handler(commands=["start"])
def start(message):
    bf.sending_start_message(bot, message, types)
    log(message)


@bot.message_handler(content_types=["text"])
def message_handler(message):
    bf.handler(bot, message, types)
    log(message)


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    user_name = message.new_chat_member.first_name
    bot.send_message(message.chat.id, "Добро пожаловать, {0}!".format(user_name))

@bot.message_handler(content_types=["photo"])
def message_handler(message):
    bf.handler(bot, message, types)
    log(message)


@bot.message_handler(content_types=["sticker"])
def message_handler(message):
    bf.handler(bot, message, types)
    log(message)


@bot.message_handler(content_types=["document"])
def message_handler(message):
    bf.handler(bot, message, types)
    log(message)


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bf.handler(bot, message, types)
    log(message)


@bot.callback_query_handler(
    func=lambda call: call.data.startswith(calendar_1_callback.prefix)
)
def callback_inline(call: CallbackQuery):
    """
    Обработка inline callback запросов
    :param call:
    :return:
    """

    # At this point, we are sure that this calendar is ours. So we cut the line by the separator of our calendar
    name, action, year, month, day = call.data.split(calendar_1_callback.sep)
    # Processing the calendar. Get either the date or None if the buttons are of a different type
    date = calendar.calendar_query_handler(
        bot=bot, call=call, name=name, action=action, year=year, month=month, day=day
    )
    # There are additional steps. Let's say if the date DAY is selected, you can execute your code. I sent a message.
    if action == "DAY":
        bot.send_message(
            chat_id=call.from_user.id,
            text=f"Вы выбрали {date.strftime('%d.%m.%Y')}",
            reply_markup=ReplyKeyboardRemove(),
        )
        print(f"{calendar_1_callback}: Day: {date.strftime('%d.%m.%Y')}")
        return bf.addtime_function(bot, call)
    elif action == "CANCEL":
        bf.addrecord_function(bot, call.message, types)
        print(f"{calendar_1_callback}: Cancellation")


@bot.callback_query_handler(func=lambda call: True)
def send_text(call, message=True):
    if call.data == "11:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 11:00")
        return bf.seanstime_function(bot, call)
    if call.data == "11:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 11:30")
        return bf.seanstime_function(bot, call)
    if call.data == "12:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 12:00")
        return bf.seanstime_function(bot, call)
    if call.data == "12:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 12:30")
        return bf.seanstime_function(bot, call)
    if call.data == "13:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 13:00")
        return bf.seanstime_function(bot, call)
    if call.data == "13:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 13:30")
        return bf.seanstime_function(bot, call)
    if call.data == "14:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 14:00")
        return bf.seanstime_function(bot, call)
    if call.data == "14:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 14:30")
        return bf.seanstime_function(bot, call)
    if call.data == "15:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 15:00")
        return bf.seanstime_function(bot, call)
    if call.data == "15:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 15:30")
        return bf.seanstime_function(bot, call)
    if call.data == "16:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 16:00")
        return bf.seanstime_function(bot, call)
    if call.data == "16:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 16:30")
        return bf.seanstime_function(bot, call)
    if call.data == "17:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 17:00")
        return bf.seanstime_function(bot, call)
    if call.data == "17:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 17:30")
        return bf.seanstime_function(bot, call)
    if call.data == "18:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 18:00")
        return bf.seanstime_function(bot, call)
    if call.data == "18:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 18:30")
        return bf.seanstime_function(bot, call)
    if call.data == "19:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 19:00")
        return bf.seanstime_function(bot, call)
    if call.data == "19:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 19:30")
        return bf.seanstime_function(bot, call)
    if call.data == "20:00":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 20:00")
        return bf.seanstime_function(bot, call)
    if call.data == "20:30":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 20:30")
        return bf.seanstime_function(bot, call)
    if call.data == "60":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 60")
        bot.send_message(chat_id=call.message.chat.id, text="Пожалуйста укажите как вас зовут:")
    if call.data == "90":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 90")
        bot.send_message(chat_id=call.message.chat.id, text="Пожалуйста укажите как вас зовут:")
    if call.data == "120":
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали 120")
        bot.send_message(chat_id=call.message.chat.id, text="Пожалуйста укажите как вас зовут:")


# @bot.callback_query_handler(func=lambda call: True)
# def callback_inline(call: CallbackQuery):
bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

if __name__ == "__main__":
    main()
    bot.polling(none_stop=True)
