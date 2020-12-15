#!/bin/bash

echo "正在进行数据分析..."
hive -e "
use ruozedata;

drop table if exists province;
create table province as
select province_code,province_name
from ruozedata_area
group by province_code,province_name;

drop table if exists analyze_t1;
create table analyze_t1 as
select provicne_id,province_name,count(orderid) as orders,round(sum(paymoney)) as payments
from ruozedata_order
join ruozedata_address on (ruozedata_order.orderid = ruozedata_address.orderMainId)
right join province on (ruozedata_address.provicne_id = province.province_code)
group by provicne_id,province_name;


drop table if exists time_detail;
create table time_detail as 
select ordertime,year(ordertime) as year,month(ordertime) as month,day(ordertime) as day,hour(ordertime) as hour,minute(ordertime) as minute,second(ordertime) as second,weekofyear(ordertime) as week
from ruozedata_order as a;

drop table if exists analyze_t2;
create table analyze_t2 as
select year,month,count(ruozedata_order.orderid) as orders,round(sum(ruozedata_order.paymoney)) as sales
from ruozedata_order
right join time_detail on (ruozedata_order.ordertime=time_detail.ordertime)
group by time_detail.year,time_detail.month;


drop table if exists analyze_t3;
create table analyze_t3 as
select hour,count(ruozedata_order.orderid) as orders,round(sum(ruozedata_order.paymoney)) as sales
from ruozedata_order
right join time_detail on (ruozedata_order.ordertime=time_detail.ordertime)
group by time_detail.hour;


drop table if exists analyze_t4;
create table analyze_t4 as
select saleDesc,count(ruozedata_order.orderid) as orders,round(sum(ruozedata_order.paymoney)) as sales
from ruozedata_order
right join ruozedata_saleorg on (ruozedata_saleorg.saleCode=ruozedata_order.saleOrgId)
group by saleOrgId,saleDesc
order by sum(ruozedata_order.paymoney) desc
limit 20;


drop table if exists analyze_t5;
create table analyze_t5 as 
select count(customerName) as count,customerName
from ruozedata_order
group by customerName
order by count(customerName) desc
limit 50;


drop table if exists analyze_t6;
create table analyze_t6 as 
select count(street_code) as count,concat(province_name,city_name,zone_name,street_name) as address,province_name,city_name,zone_name,street_name
from ruozedata_order
join ruozedata_address on (ruozedata_order.orderid=ruozedata_address.orderMainId)
join ruozedata_area on (ruozedata_address.street_id=ruozedata_area.street_code)
group by street_code,province_name,city_name,zone_name,street_name
order by count(street_code) desc
limit 20;


drop table if exists devide_region;
create  table devide_region
(
   region_id    string,
   region_name   string,
   provicne_id    string
)
row format delimited fields terminated by '\t' 
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/devide_region/';


insert into devide_region values('1','东北地区','12');
insert into devide_region values('1','东北地区','17');
insert into devide_region values('1','东北地区','18');
insert into devide_region values('2','西北地区','14');
insert into devide_region values('2','西北地区','23');
insert into devide_region values('2','西北地区','20');
insert into devide_region values('2','西北地区','22');
insert into devide_region values('2','西北地区','13');
insert into devide_region values('2','西北地区','19');
insert into devide_region values('3','华北地区','10');
insert into devide_region values('3','华北地区','16');
insert into devide_region values('3','华北地区','11');
insert into devide_region values('3','华北地区','15');
insert into devide_region values('4','华中地区','28');
insert into devide_region values('4','华中地区','29');
insert into devide_region values('4','华中地区','24');
insert into devide_region values('5','华东地区','21');
insert into devide_region values('5','华东地区','26');
insert into devide_region values('5','华东地区','27');
insert into devide_region values('5','华东地区','25');
insert into devide_region values('5','华东地区','33');
insert into devide_region values('5','华东地区','30');
insert into devide_region values('5','华东地区','35');
insert into devide_region values('6','华南地区','31');
insert into devide_region values('6','华南地区','34');
insert into devide_region values('6','华南地区','32');
insert into devide_region values('7','西南地区','36');
insert into devide_region values('7','西南地区','38');
insert into devide_region values('7','西南地区','37');
insert into devide_region values('7','西南地区','39');

drop table if exists analyze_t7;
create table analyze_t7 as 
select region_name,count(region_name) as orders_amount
from ruozedata_order
join ruozedata_address on (ruozedata_address.orderMainId=ruozedata_order.orderid)
join devide_region on (devide_region.provicne_id=ruozedata_address.provicne_id)
group by region_name;


drop table if exists analyze_t8;
create table analyze_t8 as 
select region_name,sum(paymoney) as total_payment
from ruozedata_order
join ruozedata_address on (ruozedata_address.orderMainId=ruozedata_order.orderid)
join devide_region on (devide_region.provicne_id=ruozedata_address.provicne_id)
group by region_name;
"
echo "数据分析完毕！"

echo "正在将Hive结果表导出为csv文件..."
sh turn2csv.sh
echo "导出完毕！"

















