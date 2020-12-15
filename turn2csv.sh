hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t1" | sed 's/[\t]/,/g'  > analyze_t1.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t2" | sed 's/[\t]/,/g'  > analyze_t2.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t3" | sed 's/[\t]/,/g'  > analyze_t3.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t4" | sed 's/[\t]/,/g'  > analyze_t4.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t5" | sed 's/[\t]/,/g'  > analyze_t5.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t6" | sed 's/[\t]/,/g'  > analyze_t6.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t7" | sed 's/[\t]/,/g'  > analyze_t7.csv

hive -e "
use ruozedata;
set hive.cli.print.header=true; 
select * from analyze_t8" | sed 's/[\t]/,/g'  > analyze_t8.csv

