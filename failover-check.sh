#!/bin/bash
  
if PGPASSFILE={$path-to-pgpass} psql -h {$HOSTNAME} -U postgres -d postgres -c "INSERT INTO masterchecker (datestamp) VALUES (NOW());" ; then
    echo success
else
   echo "Postgres Failover has occurred in the PG Cluster" |  mail -s "Postgres Failover has occurred in the PG Cluster" email@example.com
fi
