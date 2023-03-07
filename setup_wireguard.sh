wg genkey > /data/private
wg pubkey < /data/private > /data/public
ip -p link add wg0 type wireguard