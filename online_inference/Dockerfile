FROM python:3.7-slim

RUN pip install --no-cache-dir fastapi uvicorn joblib scikit-learn

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
