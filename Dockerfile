# pull the official base image
FROM python:3.9.0

# set environment variables
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app
EXPOSE 8000

# install dependencies
RUN set -ex && apt-get update && apt-get install -y python3-dev default-libmysqlclient-dev build-essential
RUN pip install --upgrade pip
COPY ./requirements.lock /app/requirements.lock
RUN pip install -r requirements.lock

# copy project
COPY . /app/

RUN chmod +x docker-entrypoint.sh

# ENTRYPOINT ["sh", "/app/docker-entrypoint.sh"]
CMD ["/app/docker-entrypoint.sh"]
# RUN python manage.py migrate