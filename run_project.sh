#!/bin/bash

while true
do
printf "========================================================================================\n"
printf "#############################Hadoop大作业  商业订单分析系统#############################\n"
printf "========================================================================================\n"
printf "【选择系统】\n\n"
printf "1.运行【订单分析系统】\n"
printf "\n\n"
printf "2.进入【订单查询系统】\n"
printf "\n\n"
printf "3.退出程序\n"
printf "========================================================================================\n"

read -p "请选择系统 > " pin

if [ "$pin" -eq "1" ]; then
source ./ruozedata.properties

#创建ruozedata_bi数据库
echo "message：正在创建ruozedata_bi数据库..."
mysql -u${mysql_username} -p${mysql_password} -e "
drop database if exists ruozedata_bi;
create database ruozedata_bi;
show databases;"

echo "message：正在向ruozedata_bi数据库中导入数据..."
mysql -u${mysql_username} -p${mysql_password} ruozedata_bi < ./import_data.sql
echo "message：数据导入完毕！"

echo "message：正在上传到HDFS..."
sh update2HDFS_all.sh
echo "message：上传成功！"

echo "message：创建Hive数据库..."
hive -e "
drop database if exists ruozedata;
create database ruozedata;
"
echo "message：正在创建Hive表并关联HDFS数据..."
hive -f hive_createtab.sql
echo "message：完成操作！"

echo "message：正在进行数据分析..."
sh analyze_data.sh
echo "message：数据分析完毕！"

echo "message：正在生成可视化视图..."
python3 hadoop_visualization.py
echo "message：生成完毕！已经把生成的html文件存储到工作目录中"

elif [ "$pin" -eq "2" ]; then
echo "message：初始化系统..."
sh init_orderManagementSystem.sh

echo "准备进入订单查询系统..."
sh orderManagementSystem.sh

elif [ "$pin" = "3" ]; then
        echo "成功退出系统！"
        exit 0
fi
done















