# Purpose: Automate checking network devices | servers | websites using ping, http requests, arp
# Env: Windows
# Requirement: Install Python to your Windows.
#
# #####################################################################
#
# Python libraries to be installed if not yet: json, requests, vymgmt
# To install python libraries: Go to your command prompt and type in:
#               python3 install <libray_stated_above>
#
# #####################################################################

## Remove "##" from the line below for Linux env.
## #!/usr/bin/python3
try:
    from subprocess import *
    from netmiko import *
    import requests
    import re
    import json
    import sys

except ImportError as i_err:
    print(i_err)

#Load IP Address details.
with open("ip_address.json", "r") as data_file:

    #To be loaded.
    data = json.load(data_file)

with open("vyos.json", "r") as vyos_login:
    vyos = json.load(vyos_login)

class Check:
    def __init__(self, details):
        self.details = details
    

    def ping_ip(self):
        #Send icmp requests.
        ip_addr = Popen(['ping', '-n', '1', self.details], stdout=PIPE, stderr=PIPE)
        output, error = ip_addr.communicate()

        if "Request timed out" in str(output) or \
            "Destination host unreachable" in str(output):
            print(f"{self.details} --- Host Unreachable")
        else:
            print(f"{self.details} --- Ok.")
    

    def check_websites(self):
        # Check status code of websites --- 200 = Ok.
        sites = requests.get(self.details)

        if sites.status_code == 200:
            print(f"{sites} --- Ok")
        
        else:
            print("DD")


    def check_mac_addr(self):
        pass

    def openvpn_connection(self):
        # check openvpn connection from the client sites.

        # add host and dump to existing json data. 
        # purpose: for security
        vyos_details = vyos["host"]=self.details

        json.dumps(vyos_details)
        
        vyos_conn = ConnectHandler(**vyos)

        openvpn_status = "show openvpn server status"

        ovpn_stat = vyos_conn.send_command(openvpn_status)
        return ovpn_stat







