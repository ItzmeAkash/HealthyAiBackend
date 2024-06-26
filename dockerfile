FROM python:3.10.6-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /healthyai

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:8000 

EXPOSE 8000



























