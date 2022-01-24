# 👐TBot_SalonSupport #
Телеграм бот для записи в массажный кабинет
##  ✨Функционал ##
Обзор всех функций можно найти здесь .
##  🚩Установка ##
####  📃Требования ####
* Для беспрерывной работы бота понадобится компьютер включенный 24/7, выступающий в роли сервера(VPS)
* OS - Ubuntu(Возможен запуск на Windows)
* [Git](https://git-scm.com)
* [Python 3.8](https://www.python.org)
* Интернет-соединение
* Токен Telegram бота (можно получить на [@Botfather](https://t.me/Botfather))
* ID Группы для отправки обьявлений

####  📝Подготовка ####

   - Загружаем файлы проекта на сервер:

```
git clone https://github.com/shamandok/TBot_SalonSupport.git
```
   - Переходим в каталог загруженного проекта:

```
cd TBot_SalonSupport
```
   - Создадим новое виртуальное окружение для Python:

```
python3.8 -m venv venv
```
   - Активируем его:

```
source venv/bin/activate

```
   - Запускаем авто-установщик библиотек необходимых для работы бота:
   
```
pip install -r requirements.txt

```
   - Или устанавливаем их вручную:
           
```
pip install pytelegrambotapi
pip install mysql-connector-python
pip install coloredlogs

```
####  📚База Данных ####
   - Создадим пользователя:
```
CREATE USER 'shamandok'@'%' IDENTIFIED BY 'shamandok';
```
   - Установим пароль для этого пользователя:
```
SET PASSWORD FOR 'shamandok'@'%' = 'pattaya2k19m17';
```
   - Выведем список существующих баз данных:
```
show databases;
```
   - Создадим базу данных с именем "massuport" и кодировкой UTF8 (RU/ENG)
```
CREATE DATABASE massuport CHARACTER SET utf8 COLLATE utf8_general_ci;
```
   - Выдадим разрешения нашему пользователю к созданной базе данных, с "%" - любого хоста:
```
GRANT ALL PRIVILEGES ON massuport.* TO 'shamandok'@'%';
```
   - Начиная с Ubuntu 20.04 (используется Mysql 8) изминился запрос:
```
GRANT ALL PRIVILEGES ON massuport.* TO 'shamandok'@'%' WITH GRANT OPTION;
```
   - Выберем нашу базу данных:
```
use massuport;
```
   - Создадим таблицу "masuser"
```
CREATE TABLE masuser (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(50), time VARCHAR(50), seans VARCHAR(150), uzername VARCHAR(255), komments VARCHAR(255), kontakt VARCHAR(50), user_id INT(11));
```
   -  Для очистки таблицы "masuser" от записей:
```
TRUNCATE TABLE masuser;
```
####  ⚙️Настройки ####
   -  Откроем файл с настройками бота:
```
nano config.ini
```
В настройках важно указать полный путь к папке photos!
Если используется Ubuntu, для отображения полного пути в терминале выполнить команду:
```
pwd
```
   - Для пересылки сообщений в группу добавить бота в администраторы группы и предоставить доступ к сообщениям!
####  🚀Запуск бота ####
После установки и настройки бота, для запуска вам необходимо:
   - Открыть каталог с проектом бота
```
cd TBot_dating
```
   - Активировать virtualenv (если он еще не активирован в текущем сеансе консоли):\
```
source venv/bin/activate
```
   - Деактивировать virtualenv (если он активирован в текущем сеансе консоли):\
```
deactivate
```
   - Запустить бот:
```
python -OO bot.py
```
   - Для корректной остановки работы бота используйте комбинацию:
```
Ctrl + C
```

##  ⭐Планы ##
|      Модуль     | Описание                 | Заметки                       |  Статус |
| :-------------: |:------------------------:|:-----------------------------:|:-------:|
| Локализация     | Поддержка других языков  |    (RU/END/UKR)               |    🧮   |
| Уровни доступа  | Возможности пользователей|   (User/Moderator/Admin)      |    🧮   |
| WEB-Панель      | Управление ботом         |           (AdminPanel)        |    🧮   |
|      WEB        | Страница обьявлений      |             (Site)            |    🧮   |


|       ℹ️     |            ℹ️       |         ℹ️       |       ℹ️         |        ℹ️         |
| :---------:|:------------------:|:---------------:|:---------------:|:---------------:|
|  ✔️сделано |    🛠️ В работе    |   🧮 В очереди  |  ⚡ Отладка    |    ❌Отменено   |

