#!/bin/bash

# Set the JDBC connection URL
JDBC_URL="jdbc:hive2://spark-thrift-server:10000"

# SQL command to register the Delta table
SQL="CREATE TABLE IF NOT EXISTS default.order_summary USING DELTA LOCATION 's3a://gold/warehouse/default/order_summary';"

# Run the command using beeline
beeline -u "$JDBC_URL" -n "" -p "" -d org.apache.hive.jdbc.HiveDriver -e "$SQL"

#BASH
#docker exec -it spark-master beeline -u jdbc:hive2://spark-thrift-server:10000 -e "CREATE TABLE IF NOT EXISTS default.order_summary USING DELTA LOCATION 's3a://gold/warehouse/default/order_summary';"

#docker exec -it spark-master bash -c "beeline -u jdbc:hive2://spark-thrift-server:10000 -e "CREATE TABLE IF NOT EXISTS default.order_summary USING DELTA LOCATION 's3a://gold/warehouse/default/order_summary';""