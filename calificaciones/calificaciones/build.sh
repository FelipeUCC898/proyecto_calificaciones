#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python calificaciones/manage.py collectstatic --no-input
python calificaciones/manage.py migrate