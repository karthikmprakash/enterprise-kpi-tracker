#!/bin/sh
set -e

python manage.py migrate --noinput
python manage.py initadmin
python manage.py collectstatic --noinput
exec "$@"