#!/bin/bash

echo "Waiting for MySQL..."

until nc -z db 3306; do
  sleep 2
done

echo "MySQL ready!"
python app.py