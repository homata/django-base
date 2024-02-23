# ubuntuのイメージをプルし、Pythonをインストールしていく
FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

# python3をインストール
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y --no-install-recommends python3 python3-dev \
    && source ~/.bashrc \
    && apt-get -y --no-install-recommends install vim \
    && apt-get -y --no-install-recommends install fdclone

# locale設定
RUN apt-get update &&\
    apt-get -y --no-install-recommends install locales &&\
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

# 作業ディレクトリを設定
ENV APP_HOME /src
WORKDIR $APP_HOME

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

# 依存関係のインストールとpipインストール
RUN apt install -y --no-install-recommends python3-pip
RUN apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev python3-dev libpq-dev binutils

# 地理空間ライブラリをインストールする際の依存関係
RUN apt-get install -y software-properties-common
RUN add-apt-repository ppa:ubuntugis/ppa
# RUN add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends curl python3-distutils python-is-python3 \
    && apt-get install -y --no-install-recommends libgdal-dev gdal-bin python3-gdal
# RUN apt-get install -y libgeos-dev ibproj-dev
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# pipのアップデート
RUN pip install --upgrade pip setuptools wheel
# Poetryをインストール
RUN pip install poetry
# RUN curl -sSL https://install.python-poetry.org | python -

# GDALインストール
# RUN pip install GDAL==$(gdal-config --version) --global-option=build_ext --global-option="-I/usr/include/gdal"

# $PATHに追加
ENV PATH ~/.local/bin:$PATH
# RUN echo 'export PATH="~/.local/bin:$PATH"' >> ~/.profile
RUN echo 'export PATH="~/.local/bin:$PATH"' >> ~/.bashrc

# poetryの定義ファイルをコピー (存在する場合)
# COPY pyproject.toml* poetry.lock* ./
COPY pyproject.toml*  ./

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
# コンテナ内で仮想環境の作成を無効
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.in-project true
# RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

# シェルスクリプトを実行
# COPY ./entrypoint.sh $APP_HOME/entrypoint.sh
# ENTRYPOINT ["bash", "-c", "entrypoint.sh"]
# サーバーを立ち上げる
# ENTRYPOINT ["poetry", "run", "python3", "manage.py", "runserver", "0.0.0.0:8000"]
# ENTRYPOINT ["poetry", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
