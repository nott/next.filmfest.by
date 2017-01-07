FROM fedora:24
MAINTAINER Stas Rudakou "stas@garage22.net"

ARG requirements=prod.txt

RUN dnf -y update; dnf clean all;
RUN dnf -y install python python-virtualenv gcc postgresql postgresql-devel libjpeg-devel zlib-devel mailcap redhat-rpm-config

ENV PYTHONUNBUFFERED 1

RUN useradd -d /app -m filmfest
USER filmfest
RUN virtualenv /app
RUN mkdir /app/src /app/media /app/static
WORKDIR /app/src

ADD . /app/src/
ADD IMAGE_VERSION /app/IMAGE_VERSION
RUN /app/bin/pip install -r "requirements/$requirements"

ENV DJANGO_SETTINGS_MODULE filmfest.settings.docker

RUN /app/src/docker-entrypoint.py collectstatic --noinput
ENTRYPOINT ["/app/src/docker-entrypoint.py"]
