#!/usr/bin/env python3

from netmiko import ConnectHandler
import os
import re

#host = input("Please enter hostnam or IP address: ")
user = "Gonzo185"
password = "Gonzo185!"

R1 = {
    "device_type":"cisco_ios",
    "host":"172.16.0.1",
    "username":user,
    "password":password,
}
R2 = {
    "device_type":"cisco_ios",
    "host":"10.0.0.2",
    "username":user,
    "password":password,
}
R3 = {
    "device_type":"cisco_ios",
    "host":"10.0.5.3",
    "username":user,
    "password":password,
}
R4 = {
    "device_type":"cisco_ios",
    "host":"10.0.6.4",
    "username":user,
    "password":password,
}
R5 = {
    "device_type":"cisco_ios",
    "host":"10.0.5.5",
    "username":user,
    "password":password,
}
R6 = {
    "device_type":"cisco_ios",
    "host":"10.0.6.6",
    "username":user,
    "password":password,
}

device_list = [R1, R2, R3, R4, R5, R6]

for device in device_list:
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show run")
    pattern = r"hostname ([\w-]*)"
    result = re.search(pattern, output)
    with open(f"/home/gonzo185/projects/ssh_auto/CML_Backup_configs/{result[1]}-Configs.txt", "w") as file:
        file.write(output)

print("Your CML devices are now backed up!")
