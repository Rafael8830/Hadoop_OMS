#!/bin/bash

dt=`date --date='1 days ago' +%Y-%m-%d`
date=`date +%Y%m%d -d'1 days ago'`
date="20161030"
echo ${date}

source /home/hadoop/wksp/Hadoop_task/BI_project-master/code/ruozedata.properties

sqoop export --connect ${driver_rep} --table ruozedata_dealcompany_rep -m 1 --username ${username_rep} --password ${password_rep} --export-dir /user/hive/warehouse/ruozedata.db/ruozedata_dealcompany_rep/pt_date=$date/ --input-fields-terminated-by '\t'

sqoop export --connect ${driver_rep} --table ruozedata_operatetrendandcity_rep -m 1 --username ${username_rep} --password ${password_rep} --export-dir /user/hive/warehouse/ruozedata.db/ruozedata_operatetrendandcity_rep/pt_date=$date/ --input-fields-terminated-by '\t'
<<COM
sqoop export --connect jdbc:mysql://localhost:3306/BIreport --table ruozedata_dealcompany_rep -m 1 --username root --password '123456' --export-dir /user/hive/warehouse/ruozedata.db/ruozedata_dealcompany_rep/pt_date=20161030/ --input-fields-terminated-by '\t'

sqoop export --connect jdbc:mysql://localhost:3306/BIreport --table ruozedata_operatetrendandcity_rep -m 1 --username root --password '123456' --export-dir /user/hive/warehouse/ruozedata.db/ruozedata_operatetrendandcity_rep/pt_date=20161030/ --input-fields-terminated-by '\t'
COM
