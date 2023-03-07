chmod +x wireguard/init
docker volume create wireguard-data
docker volume create mongo-data
docker compose up -d