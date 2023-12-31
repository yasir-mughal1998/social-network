FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

ENV DJANGO_SETTINGS_MODULE=social_network.settings

EXPOSE 8000
