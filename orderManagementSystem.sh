#!/bin/bash
while true
do
printf "========================================================================================\n"
printf "##################################欢迎来到订单管理系统##################################\n"
printf "========================================================================================\n"
printf "【查询选择】\n"
printf "1.查询指定日期订单信息\n"
printf "2.查询待发货订单信息\n"
printf "3.查看有订单的公司\n"
printf "4.查询公司订单信息\n"
printf "5.查看所有客户\n"
printf "6.查询客户订单信息\n"
printf "7.查看有效的地址编码\n"
printf "8.查询地址编码具体地址信息\n"
printf "9.退出系统\n"
printf "========================================================================================\n"

read -p "请选择查询项目 > " pin
if [ "$pin" -eq "1" ]; then 
	read -p "请输入要查询的日期(YYYY-MM-DD) > " para1
	hive -e "
use ruozedata;
select crt_date as orderdate,orderid,paymoney,concat(province_name,city_name,zone_name,street_name) as address,detail,customerId,customerName
from ruozedata_order
join ruozedata_address on (ruozedata_order.orderid=ruozedata_address.orderMainId)
join ruozedata_area on (ruozedata_address.street_id=ruozedata_area.street_code)
join state_detail on (state_detail.state=ruozedata_order.state)
where crt_date=\"$para1\";"
elif [ "$pin" -eq "2" ]; then
	read -p "请输入要查询的日期(YYYY-MM-DD) > " para2
	hive -e "
use ruozedata;
select crt_date as orderdate,orderid,paymoney,concat(province_name,city_name,zone_name,street_name) as address,detail
from ruozedata_order
join ruozedata_address on (ruozedata_order.orderid=ruozedata_address.orderMainId)
join ruozedata_area on (ruozedata_address.street_id=ruozedata_area.street_code)
join state_detail on (state_detail.state=ruozedata_order.state)
where crt_date=\"$para2\" and detail='待发货';
"
elif [ "$pin" -eq "3" ]; then
	hive -e "
use ruozedata;
select saleOrgId, saleDesc
from ruozedata_order
join ruozedata_saleorg on (ruozedata_saleorg.saleCode=ruozedata_order.saleOrgId)
group by saleOrgId,saleDesc;
"
elif [ "$pin" -eq "4" ]; then
	read -p "请输入需要查询的公司id  > " para4
	hive -e "
use ruozedata;
select saleOrgId,saleDesc,orderid,ordertime,paymoney,detail
from ruozedata_order
join ruozedata_saleorg on (ruozedata_order.saleOrgId=ruozedata_saleorg.saleCode)
join state_detail on (state_detail.state=ruozedata_order.state)
where saleOrgId=$para4;
"	
elif [ "$pin" -eq "5" ]; then
	hive -e"
use ruozedata;
select customerName
from ruozedata_order
group by customerName;
"
elif [ "$pin" -eq "6" ]; then
	read -p "请输入需要查询的客户名  > " para6
	hive -e"
use ruozedata;
select customerName,orderid,ordertime,paymoney,detail
from ruozedata_order
join state_detail on (state_detail.state=ruozedata_order.state)
where customerName=\"$para6\";
"
elif [ "$pin" -eq "7" ]; then
	hive -e"
use ruozedata;
select street_code from ruozedata_area;
"
elif [ "$pin" -eq "8" ]; then
	read -p "请输入需要查询的地址编码  > " para8
	hive -e"
use ruozedata;
select concat(province_name,city_name,zone_name,street_name) as address
from ruozedata_area
where street_code=$para8;
"
elif [ "$pin" = "9" ]; then 
	echo "成功退出系统！"
	exit 0
fi
done
