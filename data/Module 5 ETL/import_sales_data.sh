#!/bin/bash

# MySQL credentials
MYSQL_USER="root"
MYSQL_PASSWORD="uh6tqyfE07NuIm4PhCgV3lR1"
MYSQL_HOST="172.21.26.137"
MYSQL_PORT="3306"

# SQL file to import
SQL_FILE="sales.sql"

# Function to execute MySQL commands
mysql_command() {
  mysql -u "$MYSQL_USER" -p"$MYSQL_PASSWORD" -h "$MYSQL_HOST" -P "$MYSQL_PORT" "$@"
}

# Login to MySQL
echo "Logging into MySQL..."
mysql_command -e "exit"

# Create the "Sales" database
echo "Creating 'Sales' database..."
mysql_command -e "CREATE DATABASE Sales"

# Use the "Sales" database
echo "Using 'Sales' database..."
mysql_command Sales -e "source $SQL_FILE"

echo "Data import completed."