Helper script to take output of this query
```
mysql -h <host> -u <user> -p <database> -e "select DAY(datetime) as day, MONTH(datetime) as month, YEAR(datetime) as year, count(distinct ckey) as number, server_port as server from ss13connection_log where datetime > DATE_SUB(NOW(),INTERVAL 1 YEAR) group by month, year, day, server_port order by month, year, day;" -B > daily.tsv
```
And convert into a table organised by date -> server, for easy conversion to graphs
