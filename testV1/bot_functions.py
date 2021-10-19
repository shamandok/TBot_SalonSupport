# -*- coding: utf-8 -*-
import datetime
from keyboa.keyboards import keyboa_maker
import inscriptions
import logging
from bot import calendar, calendar_1_callback
from enum import Enum

log = logging.getLogger("bot_functions")


class States(Enum):
    """
    Мы используем БД Vedis, в которой хранимые значения всегда строки,
    поэтому и тут будем использовать тоже строки (str)
    """
    S_START = "0"  # Начало нового диалога
    S_MENU = "1"
    S_CONTACT = "1"
    S_FAQ = "1"
    S_ADD_RECORD = "2"
    S_CHOISE_DATA = "3"
    S_CHOISE_TIME = "3"
    S_CHOISE_DURATION = "3"
    S_CLIENT_NAME = "3"
    S_CLIENT_CONTACT = "3"
    S_CONFIRM_RECORD = "3"
    S_MY_RECORDS = "2"


# Функция /хэндлер/ ловит все вводы в чате
def handler(bot, message, types):
    if message and message.text:
        checking_messages(bot, message, types)
    if message and message.photo:
        checking_messages(bot, message, types)
    if message and message.sticker:
        checking_messages(bot, message, types)
    if message and message.document:
        checking_messages(bot, message, types)


def sending_start_message(bot, message, types):
    markup = menu_list_buttons(types)
    bot.send_message(message.chat.id, inscriptions.start_text.format(message.from_user), parse_mode='html',
                     reply_markup=markup)


def menu_central(bot, message, types):
    markup = menu_list_buttons(types)
    bot.send_message(message.chat.id, inscriptions.menu_central_text.format(message.from_user), parse_mode='html',
                     reply_markup=markup)


# def start_func(message):
#    if not if_user_exists(message.chat.id):
#        new_user(message.chat.id, message.from_user.first_name, message.from_user.username, None)


def menu_list_buttons(types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item1 = types.KeyboardButton(inscriptions.add_record)
    item2 = types.KeyboardButton(inscriptions.my_records)
    item3 = types.KeyboardButton(inscriptions.faq)
    item4 = types.KeyboardButton(inscriptions.contacts)
    markup.add(item1, item2, item3, item4)
    return markup


def addrecord_function(bot, message, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    todeybtn = types.KeyboardButton(inscriptions.todeybtn)
    seldatebtn = types.KeyboardButton(inscriptions.seldatebtn)
    menubtn = types.KeyboardButton(inscriptions.menubtn)
    markup.add(todeybtn)
    markup.add(seldatebtn)
    markup.add(menubtn)
    bot.send_message(message.chat.id, inscriptions.addrecord_text, parse_mode='html', reply_markup=markup)


# def timerange_function(range):
times = []
for i in range(11, 21):
    times.append(f'{i}:00')
    times.append(f'{i}:30')


def addtime_function(bot, call):
    kb_times = keyboa_maker(items=times, items_in_row=5, copy_text_to_callback=True)
    bot.send_message(chat_id=call.from_user.id, reply_markup=kb_times, text="Выберете время:")


seans = ["60", "90", "120"]


def seanstime_function(bot, call):
    kb_seanstime = keyboa_maker(items=seans, copy_text_to_callback=True)
    bot.send_message(chat_id=call.from_user.id, reply_markup=kb_seanstime, text="Выберете продолжительность сеанса:")


def seldate_function(bot, message):
    now = datetime.datetime.now()
    # Get the current date
    bot.send_message(
        message.chat.id,
        "Selected date",
        reply_markup=calendar.create_calendar(
            name=calendar_1_callback.prefix,
            year=now.year,
            month=now.month,  # Specify the NAME of your calendar
        ),
    )


def faq_function(bot, message, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menubtn = types.KeyboardButton(inscriptions.menubtn)
    markup.add(menubtn)
    bot.send_message(message.chat.id, inscriptions.faq_text, parse_mode='html', reply_markup=markup)


# Функция кнопки контакты
def contacts_function(bot, message, types):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menubtn = types.KeyboardButton(inscriptions.menubtn)
    markup.add(menubtn)
    bot.send_message(message.chat.id, inscriptions.contacts_text, parse_mode='html', reply_markup=markup)


# Функция проверки сообщений /валидатор/ прописывать все вводы тут? или только сообщения
def checking_messages(bot, message, types):
    # Main buttons
    if message.text == inscriptions.add_record:
        return addrecord_function(bot, message, types)
    if message.text == inscriptions.contacts:
        return contacts_function(bot, message, types)
    if message.text == inscriptions.faq:
        return faq_function(bot, message, types)
    if message.text == inscriptions.menubtn:
        return menu_central(bot, message, types)
    if message.text == inscriptions.seldatebtn:
        return seldate_function(bot, message)
#    else:
#        bot.send_message(message.chat.id, inscriptions.unrecognized_msg, parse_mode='html')
