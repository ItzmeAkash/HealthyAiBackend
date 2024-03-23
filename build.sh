#!/bin/bash

#build the project
echo "building the project"
python -m pip install -r requirements.txt

echo "Make Migrations...."

python manage.py makemigrations --noinput
python manage.py migrate --noinput


echo "Collecting static files"

python manage.py collectstatic --noinput --clear
