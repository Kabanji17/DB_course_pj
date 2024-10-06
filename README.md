# проект DB_course_pj

## Описание проекта
Приложение по работе с вакансиями и базой данных. Приложение получает данные по вакансиям по API с сервисов hh. Заполняет базу данных данными работодателей (компаний) и их вакансиями. Приложение позволяет делать выборку по базе данных вакансий по определённым критериям.

Разработаны классы, позволяющие проводить операции по:

получению данных по вакансиям по API с сервисов hh;
созданию базы данных и таблиц в ней;
заполнению базы данных данными о компаниях и их вакансиях;
получению выборки из базы данных.
Функция взаимодействия с пользователем при запуске приветствует пользователя и даёт краткое описание работы программы. Далее функция запрашивает название базы данных, создаэт базу и таблицы, заполняет их вакансиями выбранных работодателей*. Далее функция даёт описание возможных выборок из базы данных и запрашивает номер желаемой выборки и ключевое слово при необходимости.

Для сокрытия данных необходимых для подключения к базе данных применён конфигурационный файл ini.

### Структура проекта
```
.
├── src
│ ├── __init__.py
│ ├── base_hh_api.py
│ ├── config.py
│ ├── connect_db.py
│ ├── dbmanager.py
│ └── hh_api.py
├── tests
│ ├── __init__.py
├── .venv/
├── .env
├── .env_template
├── .git/
├── .idea/
├── .flake8
├── .gitignore
├── pyproject.toml
├── poetry.lock
├── main.py
└── README.md
```
## Установка:
1. Клонируйте репозиторий:
```
https://github.com/Kabanji17/DB_course_pj.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```
## Использование:
запустите 'main.py' и следуйте инструкциям на экране.

## Документация:
Для получения дополнительной информации обратитесь к [документации](docs/README.md).

## Лицензия:

Этот проект лицензирован по [лицензии MIT](LICENSE).