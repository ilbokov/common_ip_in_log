# common_ip_in_log
Программа выдает 10 IP-адресов, совершивших наибольшее количество запросов к указанному хосту указанным методом
## Запуск
### Склонируйте репозиторий
* git clone https://github.com/ilbokov/common_ip_in_log.git
### Создайте виртуальное окружение (для этого должен быть установлен python)
* python -m venv env
### Запустите виртуальное окружение
#### Для Windows
* .\env\Scripts\activate
#### Для Linux
* . env/bin/activate
### Установите необходимые зависимости
* pip install -r requirements.txt
### Создайте .env файл по примеру .env.template
Укажите необохдимые параметры:
- FILE_NAME
    - Имя файла с логами
- HOST
    - Адрес сайта, к которому было совершено обращение
- ENCODING
    - Кодировка файла - cp1251 или utf-8
- TYPE
    - Тип запроса (прим. GET)
### Запустите программу
* python program.py