FROM python:3.7.3

# install environment dependencies
RUN apt-get update -yqq \
  && apt-get install -yqq --no-install-recommends \
    netcat \
  && apt-get -q clean

# set working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add requirements
COPY ../requirements/requirements-dev.txt /usr/src/app/requirements-dev.txt

# install requirements
RUN pip install -r requirements-dev.txt

# Copy the tox.ini and run it
COPY ./tox.ini  /usr/src/app/tox.ini
RUN tox --notest

# add entrypoint.sh
COPY ./docker/app/entrypoint.sh /usr/src/entrypoint.sh

# add the logging config
COPY ./logging_config/logging-docker.yaml /usr/src/logging.yaml

# Copy the seeds folder to the app
COPY ./seeds  /usr/src/seeds

# run server
CMD ["../entrypoint.sh"]
