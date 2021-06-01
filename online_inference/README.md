## HW2 - Online inference

#### Запуск скрипта для запроса к сервису
```console
(env) ad@lts20-04:~/made_ml_prod/hw2$ python post_predict.py -h
usage: post_predict.py [-h] [-age AGE] [-chol CHOL] [-sex SEX] host

CLI client for heart disease prediction.

positional arguments:
  host        hostname for api request

optional arguments:
  -h, --help  show this help message and exit
  -age AGE    age (range 0 - 150)
  -chol CHOL  cholesterol level(range 0 - 1000)
  -sex SEX    gender ('m' or 'f')

```
```console
(env) ad@lts20-04:~/made_ml_prod/hw2$ python post_predict.py localhost
SEX:m AGE:75 CHOL:500 - Sick
```

#### Валидация входных данных
```console
(env) ad@lts20-04:~/made_ml_prod/hw2$ python post_predict.py localhost -sex=n -chol=-3 -age=200
status code: 422
value_error:age:age must be between 0 - 150
value_error:chol:chol must be between 0 - 2000
value_error:sex:sex must be "f" or "m"
```

#### Создание образа (локально)
```console
docker build . alekxd/hw2:latest
```

#### Pull & Run from hub.docker.com
```console
docker pull alekxd/hw2:latest
docker run -d -p 80:80 alekxd/hw2:latest
```

#### Оптимизация размера docker image
|Образ|Размер|
| ----------------- | :-----: |
|base, обычный python дистрибутив|1.23 GB|
|slim, "усеченый" python дистрибутив|470MB|
|slim-no-cache, установка пакетов без кеширования - RUN pip install --no-cache-dir | 394MB|

```console
(env) ad@lts20-04:~/made_ml_prod/hw2$ docker image ls
REPOSITORY          TAG                 IMAGE ID            SIZE
alekxd/hw02         base                b80a71327fab        1.23GB
alekxd/hw02         slim                812696e3b4e1        470MB
alekxd/hw02         slim-no-cache       b63a04400bd4        394MB
```

#### САМООЦЕНКА 
| Task| Score|
| ----------------- | :-----: |
|inference модели в rest сервиc|3/3|
|тест для /predict|3/3|
|скрипт для запросов к сервису|2/2|
|валидация входных данных|3/3|
|создание dockerfile и запуск контейнера|4/4|
|оптимизация размера docker image|3/3|
|публикация на hub.docker.com|2/2|
|readme docker pull/run|1/1|
|самооценка|1/1|
|**ИТОГО**|**22/22**|

