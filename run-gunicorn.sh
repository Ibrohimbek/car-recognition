#!/bin/bash

NAME="production"
HOMEDIR=/projects
DJANGODIR=${HOMEDIR}/car-recognition
VIRTUALENV=${HOMEDIR}/virtualenvs/production
BINDIR=${VIRTUALENV}/bin
SOCKFILE=${HOMEDIR}/run.sock
LOGFILE=${HOMEDIR}/logs/gunicorn.log

USER=recognizer
GROUP=projects
NUM_WORKERS=5
TIMEOUT=300

DJANGO_SETTINGS_MODULE=recognition.settings.production
DJANGO_WSGI_MODULE=recognition.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source ${BINDIR}/activate

export DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec ${BINDIR}/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --user $USER --group $GROUP \
  --log-level info \
  --timeout ${TIMEOUT} \
  --log-file ${LOGFILE} \
  --bind unix:$SOCKFILE \
  --workers ${NUM_WORKERS} \
  --settings ${DJANGO_SETTINGS_MODULE}
