# **Проект «API для Yatube»**
#### api_final_yatube
---
---
### Описание

##### Идея проекта
Социальная сеть для публикации личных дневников.
Пользователи могут подписываться на авторов и комментировать их записи.

##### Задача проекта
Создание api для обработки запросов

---

### Установка

##### Требования для корректной работы

[python 3.7](https://www.python.org/downloads/), django 3.2

##### Для тестирования запросов можно использовать
[Postman](https://www.postman.com/downloads/)

##### Запуск проекта
(_чек-боксы для отметки выполненного_)

[ ] _Клонировать репозиторий: `git clone` https://github.com/AlGenSo/api_final_yatube.git_
[ ] _Перейти в него в командной строке: `cd api_final_yatube`_
[ ] _Cоздать виртуальное окружение: `python -m venv venv`_
[ ] _Активировать виртуальное окружение: `. venv/Scripts/activate`_
[ ] _Обновить pip: `python -m pip install --upgrade pip`_
[ ] _Установить зависимости из файла requirements.txt: `pip install -r requirements.txt`_
[ ] _Выполнить миграции: `python manage.py migrate`_
[ ] _Запустить проект: `python manage.py runserver`_

---

### Примеры. 
##### Некоторые примеры запросов к API.

_Когда вы запустите проект, по адресу http://127.0.0.1:8000/redoc/ будет доступна документация для API Yatube._

|Запрос|Тип|Результат|Body|
|:----:|:----:|:----:|:----:|
|`/api/v1/posts/`|GET|Получить список всех публикаций.|`---`|
|`/api/v1/posts/`|POST|Добавление новой публикации в коллекцию публикаций.|`{"text": "string", "image": "string", "group": 0 }`|
|`/api/v1/posts/{id}/`|DELETE|Удаление публикации по id.|`---`|
|`/api/v1/follow/`|POST|Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса.|`{"following": "string"}`|
|`/api/v1/posts/{post_id}/comments/{id}/`|PUT|Обновление комментария к публикации по id.|`{"text": "string"}`|
|`/api/v1/token/`|POST|Получение JWT-токена.|`{"username": "string", "password": "string"}`|
