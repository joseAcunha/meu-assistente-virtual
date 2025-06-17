FROM python:3.9-slim-buster

WORKDIR /app

COPY deploy/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api:app", "--host", "0.0.00", "--port", "8000"]