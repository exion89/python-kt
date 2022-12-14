from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    #"use_keys": True,
    #"key_file": "/home/lundy/.ssh/test_rsa",
    "fast_cli": True,
    "device_type": 'cisco_ios',
    "global_delay_factor": 2
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt)

cfg = [
    'logging buffered 20000',
    'no logging console',
    'clock timezone PST -8 0'
]

output = net_connect.send_config_set(cfg)

# Send commands from file
#output = net_connect.send_config_from_file(config_file='commands.txt')

print(output)

save_out = net_connect.save_config()
print(save_out)


net_connect.disconnect()