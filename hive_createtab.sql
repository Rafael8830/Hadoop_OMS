use ruozedata;

--==============================================================--
-- Table: ruozedata_order                            --
--==============================================================--
drop table if exists ruozedata_order;
create external table ruozedata_order
(  
   orderid              string,
   ordertime            string,
   orderBelongType      string,
   saleOrgId            string,
   orderCustomerType    string,
   customerId           string,
   customerName         string,
   paymoney             string,
   state                string,
   subOrder             string
)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/ruozedata_order/';

--==============================================================--
-- Table: ruozedata_orderdetail                         --
--==============================================================--
drop table if exists ruozedata_orderdetail;
create external table ruozedata_orderdetail
(
   crt_date       string,
   orderMainId    string,
   productId      string
)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/ruozedata_orderdetail/';

--==============================================================--
-- Table: ruozedata_address                        --
--==============================================================--
drop table if exists ruozedata_address;
create external table ruozedata_address
(
   crt_date       string,
   orderMainId    string,
   provicne_id    string,
   city_id        string,
   region_id      string,
   street_id      string
)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/ruozedata_address/';

--==============================================================--
-- Table: ruozedata_area                        --
--==============================================================--
drop table if exists ruozedata_area;
create  external table ruozedata_area
(
   province_code    string,
   province_name    string,
   city_code        string,
   city_name        string,
   zone_code        string,
   zone_name        string,
   street_code      string,
   street_name      string
)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/ruozedata_area/';

--==============================================================--
-- Table: ruozedata_saleorg                        --
--==============================================================--
drop table if exists ruozedata_saleorg;
create external table ruozedata_saleorg
(
   saleCode    string,
   saleDesc    string
)
row format delimited fields terminated by '\t'
lines terminated by '\n'
stored as textfile
location '/user/hive/warehouse/ruozedata.db/ruozedata_saleorg/';
