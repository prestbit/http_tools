import socket
import threading
import time

from queue import Queue
print_lock = threading.Lock
socket.setdefaulttimeout(0.25)

first_octets = input("Enter first three octets to scan: ")

with open("port_443_scan_output.txt", "w") as f:
    print("hostname, ipaddress, port", file=f)

    port = 443
    for ipaddy in range(1, 255):
        # returns host ip address
        ip = socket.gethostbyname(first_octets + str(ipaddy))
        # returns hostname if hostname exists if not returns IP address
        hostname = socket.getfqdn(first_octets + str(ipaddy))
        #ip = socket.gethostbyname(hostname)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((first_octets + str(ipaddy), port))
            print(",".join([hostname, ip, str(port)]), file=f)
            s.close()
        except:
            #pass
            print("website: ", hostname, ",", "ip address: ", ip, "port: ", port, "is closed")

        #if ipaddy % 10==0:
        #print(ipaddy)
                                
