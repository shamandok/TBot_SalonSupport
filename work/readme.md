Код:
```python
a = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
print(a)
a[0] = 'Ср'
a[1] = 'Ср'
a[2] = 'Ср'
a[3] = 'Ср'
a[4] = 'Ср'
a[5] = 'Ср'
a[6] = 'Ср'
print(a)
```
Вывод:
```
C:\Users\shamandok\AppData\Local\Programs\Python\Python38-32\python.exe "E:/SalonNew/SalonNewV4{CALENDAR WORK BITCH}/Test.py"
['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
['Ср', 'Ср', 'Ср', 'Ср', 'Ср', 'Ср', 'Ср']

Process finished with exit code 0
```
https://habr.com/ru/post/496516/

https://delaney.gitbook.io/create-telegram-bot/

https://robomongo.org

https://sqliteman.dev


Вот функция получения с сегодняшнего дня + указанные дни
```python
import datetime

def get_date(dateFormat="%d-%m-%Y", addDays=0):

    timeNow = datetime.datetime.now()
    if (addDays!=0):
        anotherTime = timeNow + datetime.timedelta(days=addDays)
    else:
        anotherTime = timeNow

    return anotherTime.strftime(dateFormat)
Применение:

addDays = 3 #days
output_format = '%d-%m-%Y'
output = get_date(output_format, addDays)
print output
```
