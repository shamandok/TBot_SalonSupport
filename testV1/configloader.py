# -*- coding: utf-8 -*-
import configparser
import logging
import os


log = logging.getLogger(__name__)
# Проверяем, существует ли файл конфигурации, и создаем его, если его нет.
if not os.path.isfile("config.ini"):
    log.debug("Creating config.ini from template_config.ini")
    # Откройте файл шаблона и создайте файл конфигурации
    with open("template_config.ini", encoding="utf8") as template_file, \
         open("config.ini", "w", encoding="utf8") as config_file:
        # Копируем файл шаблона в файл конфигурации
        config_file.write(template_file.read())
with open("config.ini", encoding="utf8") as config_file:
    config = configparser.ConfigParser()
    config.read_file(config_file)
    token = str(config["Telegram"]["token"])