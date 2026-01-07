#!/usr/bin/env bash
set -e
uv run manage.py collectstatic --noinput
uv run manage.py migrate --noinput
# uv exec nginx -g 'daemon off;'
echo "hi"
uv run gunicorn core.wsgi:application --bind 0.0.0.0:8000