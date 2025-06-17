# Приложение, позволяющее отображать древовидное меню

Использованные технологии:
- Python
- Django
- SQLite3
- Django debug toolbar
- HTML/CSS/Bootstrap
- Docker

### Инструкция по запуску:
#### С использованием Docker
1. Клонируйте репозиторий на ваш компьютер
```angular17html
git clone https://github.com/JaxckR/testTask_4.git
```
2. Перейдите в корневую директорию и запустите docker-compose
```angular17html
cd testTask_4
```
```angular17html
docker compose up
```
3. Создайте суперпользователя
```angular17html
docker exec menu-app python manage.py createsuperuser
```
#### Без использования Docker
1. Клонируйте репозиторий на ваш компьютер
```angular17html
git clone https://github.com/JaxckR/testTask_4.git
```
2. Перейдите в корневую директорию и запустите docker-compose
```angular17html
cd testTask_4
```
3. Создайте и активируйте виртуальное окружение
```angular17html
python -m venv venv
```
```angular17html
venv\Scripts\activate
```
4. Установите все зависимости
```angular17html
pip install -r requirements.txt
```
5. Перейдите в src, примените миграции и создайте суперпользователя
```angular17html
cd src/
python manage.py migrate
python manage.py createsuperuser
```
6. Запустите приложение
```angular17html
python manage.py runserver
```