#!/bin/bash
source /home/hadoop/wksp/Hadoop_task/BI_project-master/code/ruozedata.properties

V_MYSQL_DRIVER=${mysql_driver}
V_USER=${mysql_username}
V_PASSWORD=${mysql_password}

sqoop import \
--connect ${V_MYSQL_DRIVER} \
--username ${V_USER} \
--password ${V_PASSWORD} \
--table ruozedata_order \
--hive-drop-import-delims \
--delete-target-dir \
--target-dir /user/hive/warehouse/ruozedata.db/ruozedata_order/ \
--fields-terminated-by '\t' \
--lines-terminated-by '\n' \
-m 1;


sqoop import \
--connect ${V_MYSQL_DRIVER} \
--username ${V_USER} \
--password ${V_PASSWORD} \
--table ruozedata_orderdetail \
--hive-drop-import-delims \
--delete-target-dir \
--target-dir /user/hive/warehouse/ruozedata.db/ruozedata_orderdetail/ \
--fields-terminated-by  '\t' \
--lines-terminated-by '\n' \
-m 1;


sqoop import \
--connect ${V_MYSQL_DRIVER} \
--username ${V_USER} \
--password ${V_PASSWORD} \
--table ruozedata_address \
--hive-drop-import-delims \
--delete-target-dir \
--target-dir /user/hive/warehouse/ruozedata.db/ruozedata_address/ \
--fields-terminated-by '\t' \
--lines-terminated-by '\n' \
-m 1;

sqoop import \
--connect ${V_MYSQL_DRIVER} \
--username ${V_USER} \
--password ${V_PASSWORD} \
--table ruozedata_saleorg \
--hive-drop-import-delims \
--delete-target-dir \
--target-dir /user/hive/warehouse/ruozedata.db/ruozedata_saleorg/ \
--hive-overwrite \
--fields-terminated-by  '\t' \
--lines-terminated-by '\n' \
-m 1;

sqoop import \
--connect ${V_MYSQL_DRIVER} \
--username ${V_USER} \
--password ${V_PASSWORD} \
--table ruozedata_area \
--hive-drop-import-delims \
--delete-target-dir \
--target-dir /user/hive/warehouse/ruozedata.db/ruozedata_area/ \
--fields-terminated-by  '\t' \
--lines-terminated-by '\n' \
-m 1;
