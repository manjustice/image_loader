FROM python:3.11.3-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

RUN alembic upgrade head

CMD python bot.py >> bot.log 2>&1 & python main.py >> api.log 2>&1
