#!/bin/bash

python manage.py collectstatic --noinput
python manage.py migrate
echo "Starting Gunicorn for production on port 5000..."
exec gunicorn your_project.wsgi:application --bind=0.0.0.0:5000 --workers=4



