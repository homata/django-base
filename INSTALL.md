INSTALL
====

Poetry settings
---

for docker environment
```
$ cp app/pyproject.docker.toml app/pyproject.toml
```

for windows local environment
```
<backend root>\ copy app\pyproject.windows.toml app\pyproject.toml

*1 please GDAL binary module under pythonlibs directory
```

### GDAL binary module for windows
please download this site.　　

[Archived: Unofficial Windows Binaries for Python Extension Packages](https://www.lfd.uci.edu/~gohlke/pythonlibs/)  

e.g. GDAL-3.4.3-cp311-cp311-win_amd64.whl


Docker build from Dockerfile
----

make "shotengai_digital_twin_app" image.
```
e.g.
$ docker build -t <image name> .

$ cd app
$ docker build -t shotengai_digital_twin_app .
```

Docker start
```
e.g.
$ docker run -itd  --name <execute name> <image name>

$ docker run -itd  --name shotengai_digital_twin_app_setting shotengai_digital_twin_app
```

bash shell login for setting
```
$ docker exec -it shotengai_digital_twin_app_setting bash
```

check Poetry install
```
<container name>:/app# pip list | grep poetry
poetry               1.7.1
poetry-core          1.8.1
poetry-plugin-export 1.6.0
```

environments
----

copy environment file ".env"
```
$ cp .env.sample .env
$ vi .env
```

create loggging directory
```
$ mkdir app/logs
```

make Docker image with no cache
```
$ docker compose build --no-cache
```

poetry install for Django in docker
```
$ docker compose run --entrypoint "poetry install --no-root" shotengai_digital_twin_app
```

databae migration
```
$ docker compose run --entrypoint "poetry run python manage.py migrate" shotengai_digital_twin_app
```

collect static files
```
$ docker compose run --entrypoint "poetry run python manage.py collectstatic" shotengai_digital_twin_app
```

make admin user
```
$ docker compose run --entrypoint "poetry run python manage.py createsuperuser" shotengai_digital_twin_app
```

setting in Docker image using bash shell
```
$ docker-compose up -d
$ docker-compose exec shotengai_digital_twin_app bash
<container>:/src# poetry install --no-root
<container>:/src# poetry run python manage.py migrate
<container>:/src# poetry run python manage.py collectstatic
<container>:/src# poetry run python manage.py createsuperuser
```

docker start using docker-compose
```
$ docker compose up -d
```

check docker running
```
$ docker compose logs -f
container  | System check identified no issues (0 silenced).
container  | September 08, 2023 - 12:30:05
container  | Django version 4.2.5, using settings 'config.settings'
container  | Starting development server at http://0.0.0.0:8000/
container  | Quit the server with CONTROL-C.
container  |
```

enter Docker with bash shell
```
existing containers
$ docker-compose exec shotengai_digital_twin_app bash

container startup
$ docker-compose run shotengai_digital_twin_app bash
```
