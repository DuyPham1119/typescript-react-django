FROM python:3.9-slim

ENV PYTHONUNBUFFER 1

WORKDIR /app/backend

COPY requirements.txt ./

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
  build-essential \
  gcc

RUN python -m venv /app/env

ENV PATH="/app/env/bin:$PATH"

RUN pip install -r requirements.txt

COPY ./web_api ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]