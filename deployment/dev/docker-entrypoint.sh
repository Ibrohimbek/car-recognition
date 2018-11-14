#!/bin/sh

# Start server
echo "Starting Car-recognition backend server"
python3 manage.py runserver 0.0.0.0:8080
