## API для проекта YaTube, упакованное в контейнер Docker
![master push workflow status](https://github.com/tWoAlex/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)

Проект является бэкендом портала обзоров на различные произведения искусства, включающий систему публикации сведений о произведении, обзоров и комментариев к ним.
Включает в себя базу данных и открытый API.

### API позволяет:
* Администраторам: публиковать сведения о произведениях
* Получить сведения об оцениваемых произведениях
* Публиковать обзоры и рецензии
* Публиковать комментарии к обзорам и рецензиям

### Документация проекта:
Доступна по адресу
```
http://{{ URL или IP вашего сервера }}/redoc/
```
После запуска проекта.

Мой тестовый сервер:
```
http://158.160.64.247
```

### Как запустить проект:
1. Установите Docker и Docker Compose по [официциальной инструкции](https://docs.docker.com/compose/install/).
2. Создайте на личном сервере папку для размещения конфигурации проекта.
3. Склонируйте в неё содержимое папки **infra/**.
4. Перейдите в папку и вызовите команду:
```
sudo docker-compose stop            # для остановки предыдущей версии
sudo docker pull twoalex/api_yamdb  # для загрузки актуального образа
sudo docker-compose up -d           # для запуска актуальной версии
```
5. Первый запуск, подготовка базы данных и суперпользователя:
```
```
6. Опционально, наполнить тестовыми данными:
```
```

### Примеры запросов:
Публикация обзора:
```
POST /api/v1/titles/{title_id}/reviews/
Тело: { "text": "Текст вашего обзора", "score": "оценка произведения" }
```
Просмотр обзоров:
```
GET /api/v1/titles/{title_id}/reviews/
Ответ:
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "score": 1,
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
```
Публикация комментария:
```
POST /api/v1/titles/{title_id}/reviews/{review_id}/comments/
Тело: { "text": "Текст вашего комментария" }
```
Просмотр комментариев:
```
GET /api/v1/titles/{title_id}/reviews/{review_id}/comments/
Ответ:
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "text": "string",
      "author": "string",
      "pub_date": "2019-08-24T14:15:22Z"
    }
  ]
}
```

### Использованные технологии:
* Django 3.2
* Django Rest Framework 3.12.4
* DRF SimpleJWT 4.7.2