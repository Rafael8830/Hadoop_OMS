hive -e "
use ruozedata;
drop table if exists state_detail;
create  table state_detail
(
   state    string,
   detail    string
)
row format delimited fields terminated by '\t' 
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/state_detail/';


insert into state_detail values('5','待发货');
insert into state_detail values('6','待收货');
insert into state_detail values('7','交易成功');
insert into state_detail values('0','其他');
insert into state_detail values('1','其他');
insert into state_detail values('13','其他');
insert into state_detail values('17','其他');
insert into state_detail values('18','其他');
insert into state_detail values('19','其他');
insert into state_detail values('20','其他');
insert into state_detail values('8','其他');
"
