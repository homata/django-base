FROM docker.io/postgres:12
ENV LANG ja_JP.UTF-8
ENV TZ Asia/Tokyo
RUN apt-get update && apt-get install locales dialog tzdata -y \
               && localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8 \
               && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

ENV LANG ja_JP.UTF-8

RUN apt update \
    && apt-get install wget vim iputils-ping net-tools unzip less -y \
    && apt-get install postgresql-12-postgis-3 -y
RUN echo "create extension if not exists postgis;" > /docker-entrypoint-initdb.d/dbinit.sql
