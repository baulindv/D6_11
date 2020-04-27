### D6.11 Домашнее задание

Проект библиотеки, адаптированный для соответствия требованиям задания 6.11

Возможности: заведение авторов, издательств, книг. Для книги можно загрузить картинку, которая будет отображаться на странице "список книг в библиотеке". Есть возможность указать друзей, кому отдана книга на чтение. Добавление / Обновление информации - через стандартную админку django.

Список необходимых модулей для работы проекта находится в файле requirements.txt

Для запуска использовать команду "python manage.py runserver". Главная страница проекта будет доступна по адресу http://127.0.0.1:8000/

Логин: пароль для доступа в админку: 1:1

Выполнены пункты домашнего задания:

1. CSS-стили bootstrap раздаются через STATIC для страниц библиотеки.
2. Создан базовый шаблон base.html с блоками, которые переопределены в дочерних шаблонах библиотек.
3. В модель книги добавлена возможность загружать картинки через админку. На странице "список книг в библиотеке" отображается картинка для книги, при её наличии.
4. В файле README.md создано описание проекта.