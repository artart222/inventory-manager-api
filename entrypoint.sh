#!/bin/bash
set -e

# Start Postgres in background
pg_ctlcluster 15 main start || echo "Postgres already running"

# Wait for Postgres to be ready
until pg_isready -h localhost -p 5432 >/dev/null 2>&1; do
  echo "Waiting for Postgres..."
  sleep 1
done

# Create default .env if it doesn't exist
if [ ! -f "/app/.env" ]; then
  echo "Creating default .env file..."
  cat <<EOT >> /app/.env
DEBUG=True
SECRET_KEY=$(python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())")
DB_NAME=inventory_db
DB_USER=inventory_user
DB_PASSWORD=pass
DB_HOST=localhost
DB_PORT=5432
DEBUG=True
ALLOWED_HOSTS=localhost
EOT
fi

# Run Django migrations before starting server
python api/manage.py makemigrations
python api/manage.py migrate

# Start Django server
exec python api/manage.py runserver 0.0.0.0:8000

