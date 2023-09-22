#### Задача:
Разработать Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.
##  Запуск проекта локально
## Установка
#### Шаг 1. Проверьте установлен ли у вас Docker
Прежде, чем приступать к работе, необходимо знать, что Docker установлен. Для этого достаточно ввести:
bash
docker -v
Или скачайте [Docker Desktop](https://www.docker.com/products/docker-desktop) для Mac или Windows. [Docker Compose](https://docs.docker.com/compose) будет установлен автоматически. В Linux убедитесь, что у вас установлена последняя версия [Compose](https://docs.docker.com/compose/install/). Также вы можете воспользоваться официальной [инструкцией](https://docs.docker.com/engine/install/).

#### Шаг 2. Клонируйте репозиторий себе на компьютер
Введите команду:
```bash
git clone https://github.com/Hovo-93/FileUpload.git
```
#### Шаг 3. Создайте в клонированной директории файл .env
Пример:
```bash
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
DB_NAME=file-upload
DB_PASSWORD=postgres
DB_USER=postgres
DB_HOST=db
DB_PORT=5432
```

#### Шаг 4. Запуск docker-compose
Для запуска необходимо выполнить из директории с проектом команду:
```bash
docker-compose up -d
```
#### Документация
Документация к API доступна по адресу:
json
http://localhost:8080/swagger/

##### Другие команды
Создание суперпользователя:
```bash
    docker-compose exec web python manage.py createsuperuser
```
Для пересборки и запуска контейнеров воспользуйтесь командой:
```bash
    docker-compose up -d --build 
```
Останавливаем и удаляем контейнеры, сети, тома и образы:
```bash
Stop and Delete containers

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)

Delete Images
docker rmi $(docker images -a -q)
```
## Примеры
Для формирования запросов и ответов использована программа [Postman](https://www.postman.com/).

### Загрузка файла
```json
POST http://127.0.0.1:8000/upload/
```
### Не забываем в headres добавить
```json
Content-Disposition 'attachment;filename=file'
filename file
```
### Получения списка  всех файлов с их данными, включая статус обработки.
```json
GET http://127.0.0.1:8000/files/
```


