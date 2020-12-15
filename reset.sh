source ./ruozedata.properties

#删除Hive数据库
hive -e "
drop database if exists ruozedata;
"
#删除HDFS文件夹
hdfs dfs -rm -r /user/hive/warehouse/ruozedata.db/ruozedata_*

#删除MySQL数据库
mysql -u${mysql_username} -p${mysql_password} -e "
drop database if exists ruozedata_bi;
"
