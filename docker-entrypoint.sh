#!/bin/bash
set +ex

echo "Running script bhai....."

run_local() {
    MYSQL_HOST=$(python -c "from main.settings import DATABASES; print(DATABASES['default']['HOST'])")
    until nc -z $MYSQL_HOST 3306; do sleep 1; echo "waiting for DB to come up at ($MYSQL_HOST)..."; done;

    info 'Running migrations...'
    ./manage.py migrate

    info 'Run server...'
    exec python manage.py runserver 0:8001
}

echo "Running local also"
run_local