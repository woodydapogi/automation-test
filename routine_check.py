## #!/usr/bin/python3

try:
    from netsys_check import * #From netsys_check script.
    import sys
    import requests

except ImportError as i_err:
    print(i_err)


def main():
    while True:
        options = '''
        1. Check connection via ICMP
        2. Check websites.
        3. Check MAC Address
        '''

        print("##" * 20)
        print(options)
        print("##" * 20)

        option = int(input("Option#> "))

        if option == 1:
            ping_ip_address()
        
        elif option == 2:
            check_websites()

        else:
            print("Invalid option. Exiting....")
            sys.exit()

        
def ping_ip_address():
    routers = data["routers"]
    sw = data["switch"]
    srv = data["servers"]

    ip_addrs = [
        routers,
        sw,
        srv
    ]

    try:
        for ip_add in ip_addrs:
            # indicate the device in each ip group.
            if "10.1.2.5" in ip_add:
                print("\n### Start of Switch ###")
            elif "10.0.0.1" in ip_add:
                print("### Start of Router ###")
            elif "10.0.0.2" in ip_add:
                print("\n### Start of Server ###")

            #output ip address in one list. ???
            for ip_a in ip_add:
                ip = Check(ip_a)
                ip.ping_ip()
            
    except SyntaxError as s_err:
        print(s_err)


def check_websites():
    sites = data["websites"]

    for site in sites:
        print(site)
        website = Check(site)
        website.check_websites()
        print("\n")

if __name__ == "__main__":
    main()
