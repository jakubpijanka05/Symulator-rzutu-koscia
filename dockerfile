FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txts

COPY . .

CMD ["python", "app/main.py"]
