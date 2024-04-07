# Серверная часть проекта

## Шаг 1 Установка всех зависимостей и модулей

Прежде всего, убедитесь, что у вас установлена Java JDK версии 11, так как для развертывания модели TorchServe использует Java для экспонирования своих API.
```bash
sudo apt install openjdk-11-jre-headless
```

Установка необходимых модулей для python3
```bash
pip install -r requirements.txt
```
## Шаг 2 Скачивание модели

Я использую модель RuBERT, она способна обрабатывать как русский, так и англиский текст.
https://huggingface.co/blanchefort/rubert-base-cased-sentiment-rusentiment

Создайте директорию для хранения модели
```bash
mkdir save_model
mkdir save_model/model
mkdir save_model/tokenizer
```

Чтобы скачать модель и токенизатор просто запустите файл download_model.py
```bash
python3 download_model.py
```
После этой команды модель и токенизатор будут храниться в соответсвующих директориях

## Шаг 3 Создание архива с моделью

С помощью этой команды создаем архив.
```bash
torch-model-archiver --model-name sentiment --handler handler.py -v 1.0
```
--model-name : имя модели(любое)

--handler : файл с handler

-v : версия

Создадим директорию model-store
```bash
mkdir model-store
```
Перенесем архив с моделью в model-store
```bash
mv sentiment.mar model-store/
```
## Шаг 4.1 Запуск с помощью torchserve

ВНИМАНИЕ Если вы хотите запустить сервис с помощью Docker, то перелистывается на шаг 4.2

Запуск torchserve
```bash
torchserve --start --model-store model-store --models sentiment=sentiment.mar --ts-config config.properties --ncs
```
--start : запуск

--model-store : указываем нашу директорию с моделью

--models : придумываем название модели который будет видеть torchserve и указываем на архив с моделью

--ts-config : указываем наш файл конфигураций

В моем случае в файле конфигураций я написал хост и порты для сервисов torchserve и конфигурацию CORS

## Шаг 4.2 Запуск с помощью Docker
```bash
docker compose up --build -d
```
По умолчанию у меня стоят следующие порты

8080 - inference

8081 - management

8082 - metrics

## Чтобы изменить порты:


### Для внешних портов измените порты в docker-compose.yaml

ВНИМАНИЕ меняйте именно внешние порты в docker-compose.yaml


### Для внутренних портов измените порты в docker-compose.yaml и config.properties

ВНИМАНИЕ меняйте именно внутренние порты в docker-compose.yaml


После всех манипуляций проверьте работает ли ваш сервис
```bash
curl http://0.0.0.0:8081/models/
```
Ответ должен быть ввиде json с названием вашей модели
```json
{
  "models": [
    {
      "modelName": "sentiment",
      "modelUrl": "sentiment.mar"
    }
  ]
}
```
Чтобы сделать predict создайте файл text.txt и напишите в него что-либо

Далее введите такой запрос
```bash
curl http://0.0.0.0:8080/predictions/sentiment -T example/text.txt 
```

Ответ должен быть ввиде json 
```json
{
  "data": 2
}
```
```bash
0 - Нейтрально

1 - Позитив

2 - Негатив
```
# Разработчик
tg@RuslanZalikov
