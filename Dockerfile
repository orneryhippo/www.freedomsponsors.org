FROM python:2.7
RUN pip install uwsgi
RUN apt-get update --fix-missing
RUN apt-get -y install python-dev python-lxml libxslt-dev libpq-dev pgadmin3 libtiff5-dev libjpeg62-turbo-dev zlib1g-dev libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
RUN apt-get -y install libxmlsec1-dev swig
ENV PYTHONUNBUFFERED=1
COPY docker/bin/* /usr/local/bin
WORKDIR /usr/src/app
COPY requirements-django1.10.txt requirements-django1.10.txt
RUN pip install -r requirements-django1.10.txt
ENV DATABASE_NAME=frespo
ENV DATABASE_USER=frespo
ENV DATABASE_PASS=frespo
ENV DATABASE_HOST=postgres
ENV DATABASE_PORT=5432
COPY djangoproject /usr/src/app