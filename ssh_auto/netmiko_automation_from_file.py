#!/usr/bin/env python3

from netmiko import ConnectHandler
import importlib.util
import sys

#Create module to use device list
spec = importlib.util.spec_from_file_location("CML_devices", "/home/gonzo185/Documents/Lab_Inventory/CML_devices.py")
CML_devices = importlib.util.module_from_spec(spec)
sys.modules["CML_devices"] = CML_devices
spec.loader.exec_module(CML_devices)

config_list = []

with open("router_configs", "r") as file:
    contents = file.readlines()
    for line in contents:
        config_list.append(line)

for device in CML_devices.device_list:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_set(config_list)

print("Finished!")
