FROM python:3.10-bullseye

MAINTAINER Viktor Turaev 'screenshot_994@mail.com'

RUN pip install --upgrade pip
RUN pip install poetry==1.2.2
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./


RUN poetry install

COPY . /app
WORKDIR /homework_03/app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python"]

CMD uvicorn app:app --host=0.0.0.0 --port=8000