wg genkey > /data/private
wg pubkey < /data/private > /data/public
ip -6 link add wg0 type wireguard
ip addr add fe80::1/64 dev wg0
wg set wg0 private-key /data/private
ip -6 link set wg0 up