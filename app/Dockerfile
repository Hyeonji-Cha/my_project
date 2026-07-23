FROM python:3.14.0-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

#COPY . . > 통상 사용, .dockerignore작성을 통해 필터링 함
COPY main.py .




