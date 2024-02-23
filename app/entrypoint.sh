#!/bin/sh

#if [ "$POSTGRES_NAME" = "postgres" ]
#then
#    echo "Waiting for postgres..."
#
#    while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
#      sleep 0.1
#    done
#
#    echo "PostgreSQL started"
#fi
#
#exec "$@"

echo "entrypoint.sh started"

# postgresへの接続を確認した後にマイグレーションを自動で行う
# python manage.py flush --no-input   # 全データ削除
# python manage.py migrate # データベースマイグレーション
