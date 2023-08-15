#!/bin/bash

container_name=$1

case $container_name in
  "tb_gateway_ns3_valve_1")
    echo "restart tb_gateway_ns3_valve_1"
    sh ./restart_ns3_valve/restart_ns3_valve_1.sh
    ;;
  "tb_gateway_ns3_valve_2")
    echo "restart tb_gateway_ns3_valve_2"
    sh ./restart_ns3_valve/restart_ns3_valve_2.sh
    ;;
  "tb_gateway_ns3_valve_3")
    echo "restart tb_gateway_ns3_valve_3"
    sh ./restart_ns3_valve/restart_ns3_valve_3.sh
    ;;
  "tb_gateway_ns3_valve_4")
    echo "restart tb_gateway_ns3_valve_4"
    sh ./restart_ns3_valve/restart_ns3_valve_4.sh
    ;;

esac