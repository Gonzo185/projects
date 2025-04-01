#!/usr/bin/env python3

from netmiko import ConnectHandler

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
    for n in range (3,10):
        output = net_connect.send_config_set([f"interface loopback 0", f"description HEY LET'S TRY THIS AGAIN JUST TO MAKE SURE IT'S WORKING FROM THE LINUX BOX"])
