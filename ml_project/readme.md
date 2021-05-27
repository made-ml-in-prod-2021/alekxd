### создание виртуального окружения и установка зависимостей
```
python3 -m venv .venv_hw1
source .venv_hw1/bin/activate
pip3 install -r requirements.txt
```

### запуск обучения
```
python3 src/train.py configs/all_features.yaml
```
```console
(made) ad@AD:~/hw/ml_project$ python3 src/train.py configs/min_features.yaml
INFO:root:converted data saved in: data/processed/train_data.pkl
IINFO:root:model type: RandomForestClassifier - {"n_estimators": 200, "max_depth": 5}
INFO:root:inputs shape: (227, 3), (227,)
INFO:root:model validation score: 0.5652
INFO:root:model saved in: models/model_RF.pkl
(made) ad@AD:~/hw/ml_project$ python3 src/train.py configs/all_features.yaml
INFO:root:converted data saved in: data/processed/train_data.pkl
INFO:root:model type: LogisticRegression - {"max_iter": 1000, "penalty":"l2"}
INFO:root:inputs shape: (227, 22), (227,)
INFO:root:model validation score: 0.8478
INFO:root:model saved in: models/model_LR.pkl
```

### запуск предсказания 
```
python3 src/predict.py configs/all_features.yaml
```
```console
(made) ad@AD:~/hw/ml_project$ python3 src/predict.py configs/min_features.yaml
INFO:root:converted data saved in: data/processed/test_data.pkl
INFO:root:inputs shape: (76, 3)
INFO:root:model: RandomForestClassifier
INFO:root:prediction results saved in: models/prediction_RF.csv
(made) ad@AD:~/hw/ml_project$ python3 src/predict.py configs/all_features.yaml
INFO:root:converted data saved in: data/processed/test_data.pkl
INFO:root:inputs shape: (76, 22)
INFO:root:model: LogisticRegression
INFO:root:prediction results saved in: models/prediction_LR.csv

```

### САМООЦЕНКА 
| Task| Score|
| ----------------- | :-----: |
|ветка homework1|1/1|
|описание к пулл реквесту|2/2|
|выполнение EDA|2/2|
|скрипт для генерации отчета|1/1|
|модульная структура|2/2|
|использованы логгеры|2/2|
|тесты на модули и весь пайплайн|0/3|
|генерация синтетических данных|0/3|
|разные конфиги в json или yaml|3/3|
|датаклассы для сущностей из конфига|3/3|
|кастомный трансформер|0/3|
|readme для обучения|2/3|
|readme для predict|2/3|
|используется hydra|0/3|
|настроен CI|0/3|
|самооценка|1/1|
|**ИТОГО**|**21/38**|
