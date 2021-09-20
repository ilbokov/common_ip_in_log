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
### Создайте .env файл с необходимыми параметрами по примеру .env.template
### Запустите программу