#!/usr/bin/env bash
# exit on error
# these lines were added
# Start server to upload in render
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate