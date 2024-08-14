FROM python:3.10.5-slim-buster
ADD requirements.txt /myapp/requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && python -m venv /env \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --no-cache-dir -r /myapp/requirements.txt 

ADD . /myapp
WORKDIR /myapp

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "myapp.wsgi:application"]
