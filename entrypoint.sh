#!/bin/sh
set -e

echo "Waiting for database to be ready..."
while ! python -c "import psycopg2; psycopg2.connect('$DATABASE_URI')" 2>/dev/null; do
    echo "Database not ready, waiting..."
    sleep 2
done

echo "Database is ready!"
echo "Initializing database..."
python manage.py

echo "Starting application..."
exec "$@"
