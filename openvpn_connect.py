## #!/usr/bin/python3

try:
    from netsys_check import * #From netsys_check script.
    import sys

except ImportError as i_err:
    print(i_err)

def openvpn_check():
    hq_router = Check("10.0.0.1")
    print(hq_router.openvpn_connection())


if __name__ == "__main__":
    openvpn_check()