FROM python:3.10-alpine

WORKDIR /app

ENV PYTHONDONTWIREBYTECODE=1
ENV PYTHONUNBUFFERRED=1

RUN apk update && apk add --no-cache\
    python3-dev\
    gcc\
    musl-dev\
    linux-headers\
    postgresql-dev \
    libpq-dev

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

