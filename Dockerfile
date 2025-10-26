# syntax=docker/dockerfile:1
FROM python:3.12.10-slim

# Prevent Python from writing .pyc files and buffer issues
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies + Postgres server and client
RUN apt-get update && \
    apt-get install -y postgresql postgresql-client libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# Initialize DB & create user
RUN service postgresql start && \
    su - postgres -c "psql -c \"CREATE USER inventory_user WITH PASSWORD 'pass';\"" && \
    su - postgres -c "createdb -O inventory_user inventory_db"

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy application code
COPY . .

# Make entrypoint executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose Django port
EXPOSE 8000

# Use bash entrypoint
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]
