mkdir /data/db/cfg0 /data/db/cfg1 /data/db/cfg2
mkdir /data/db/shard0 /data/db/shard1 /data/db/shard2
mkdir /data/db/log

mongod --configsvr --dbpath /data/db/cfg0 --port 27018 --fork --logpath /data/db/log/cfg0.log --replSet cfg
mongod --configsvr --dbpath /data/db/cfg1 --port 27019 --fork --logpath /data/db/log/cfg1.log --replSet cfg
mongod --configsvr --dbpath /data/db/cfg2 --port 27020 --fork --logpath /data/db/log/cfg2.log --replSet cfg

mongosh --port 27018
rs.initiate()
rs.add("localhost:27019")
rs.add("localhost:27020")
exit

mongod --shardsvr --dbpath /data/db/shard0 --port 27021 --fork --logpath /data/db/log/shard0.log --replSet shard
mongod --shardsvr --dbpath /data/db/shard1 --port 27022 --fork --logpath /data/db/log/shard1.log --replSet shard
mongod --shardsvr --dbpath /data/db/shard2 --port 27023 --fork --logpath /data/db/log/shard2.log --replSet shard

mongosh --port 27021
rs.initiate()
rs.add("localhost:27022")
rs.add("localhost:27023")
exit

mongos --configdb cfg/localhost:27018,localhost:27019,localhost:27020 --port 27024 --fork --logpath /data/db/log/mongos0.log
mongos --configdb cfg/localhost:27018,localhost:27019,localhost:27020 --port 27025 --fork --logpath /data/db/log/mongos1.log

mongosh --port 27024
sh.addShard("shard/localhost:27021")
