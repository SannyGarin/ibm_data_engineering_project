Hi there,

I'm glad you are here.

This project is about creating a simple OLTP server so there isn't much coding

Here's the code of the datadump.sh that enables me to automatically backup my simple OLTP database.

#!/bin/bash

# setting up MySQL credentials and database name

MYSQL_USER="root"
MYSQL_PASSWORD="dgGjTlUxXRGNFtVHnGYZGiYn"
MYSQL_DATABASE="Sales"
TABLE_NAME="sales_data"

# Use mysqldump to backup the specific table
mysqldump -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE $TABLE_NAME > sales_data.sql

# Log into the MySQL CLI and verify the backup
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE <<EOF
USE $MYSQL_DATABASE;
SELECT COUNT(*) FROM $TABLE_NAME;
EOF

echo "Backup completed successfully!"
