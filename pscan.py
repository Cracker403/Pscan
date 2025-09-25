import socket
import os
import termcolor
import argparse

# get ip from user
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--domain')
args = parser.parse_args()
ip = args.domain

# clear screen
os.system("cls") if os.name == "nt" else os.system("clear")

# print banner
banner = termcolor.colored(f"""
                  _  
 _ __   ___  _ __| |_   ___  ___ __ _ _ __  _ __   ___ _ __
| '_ \ / _ \| '__| __| / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
| |_) | (_) | |  | |_  \__ \ (_| (_| | | | | | | |  __/ |
| .__/ \___/|_|   \__| |___/\___\__,_|_| |_|_| |_|\___|_|
|_|
                ## Coded By >> Cracker

Target IP: {ip} 
""", 'blue')
print(banner)

 # Start Full Scan
for port in range(65535):
    try:    
        # ip V4  , TCP
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # wait 1 second
        client.settimeout(1)
        # connection with  target_ip , port { ex to rcev 0 or 1 }
        connect = client.connect_ex((ip,port))
        if connect == 0:
            # get service name by port numper
            service = socket.getservbyport(port)
            # print port-number and service
            print(termcolor.colored(f"Port: {port} => service: {service}","green"))
    except Exception :
            # print port
            print(termcolor.colored(f"Port {port} => Service name is not found", "red"))

# close connection
client.close()

