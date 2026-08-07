#!/bin/sh
set -e
python manage.py migrate --noinput
exec gunicorn -c gunicorn.conf.py guestbook.wsgi:application
