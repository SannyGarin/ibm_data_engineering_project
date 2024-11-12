#!/bin/bash

# Replace with the actual download URL
download_url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt"

# Destination directory
destination_dir="/home/project/airflow/dags/capstone"

# Create the destination directory if it doesn't exist
mkdir -p "$destination_dir"

# Download the file using wget
wget -q -O "$destination_dir/accesslog.txt" "$download_url"

# Check if the download was successful
if [ $? -eq 0 ]; then
  echo "Download completed successfully!"
else
  echo "Download failed."
fi