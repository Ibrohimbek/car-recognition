#!/bin/sh

echo "Starting server"
gunicorn --reload -b 0.0.0.0:8080 recognition.wsgi --workers 3 --timeout 300 --log-level error --log-file /opt/gunicorn.log
