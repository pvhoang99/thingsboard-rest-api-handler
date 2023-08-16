/usr/local/bin/docker-compose -f /root/thingsboard-gateway-final/docker/docker-compose-ns3-valve.yml down tb-gateway-ns3-valve-3 & wait
/usr/local/bin/docker-compose -f /root/thingsboard-gateway-final/docker/docker-compose-ns3-valve.yml up -d tb-gateway-ns3-valve-3 & wait

echo "$(date +%c) restart ns3 valve 3 done" >> /root/restart_log/restart_log.log