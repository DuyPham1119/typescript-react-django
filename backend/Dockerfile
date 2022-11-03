FROM python:3.8.7-slim-buster

ENV PYTHONUNBUFFER 1

WORKDIR /app/backend

COPY requirements.txt ./

RUN apt-get update \
  && apt-get install -y libpq-dev gcc \
  build-essential \
  gcc

RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"

RUN pip install -r requirements.txt

COPY ./web_api ./
RUN python manage.py collectstatic --no-input \
    && python manager.py makemigrations \
    && python manager.py migrate

EXPOSE 8000

CMD ["gunicorn", "-c", "config/conf.py", "--bind", ":8000", "--workers", "3", "web_api.wsgi:application"]