import joblib
from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, ValidationError, validator

PATH_TO_MODEL = 'app/model.pkl'

class Item(BaseModel):
    age: float
    chol: float
    sex: str

    @validator('sex')
    def sex_f_or_m(cls, v):
        if v not in ('m', 'f'):
            raise ValueError('sex must be "f" or "m"')
        return v

    @validator('age')
    def age_period(cls, v):
        if v < 0 or v > 150:
            raise ValueError('age must be between 0 - 150')
        return v

    @validator('chol')
    def chol_period(cls, v):
        if v < 0 or v > 2000:
            raise ValueError('chol must be between 0 - 2000')
        return v

app = FastAPI()

with open(PATH_TO_MODEL, 'rb') as f:
    model = joblib.load(f)

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "heart disease prediction"

@app.post("/predict/")
async def post_predict(item: Item):
    pred = model.predict([[item.age, item.chol, 0 if item.sex == 'm' else 1]])
    return {'target':str(pred)}
