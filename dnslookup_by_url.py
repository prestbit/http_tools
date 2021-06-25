import socket
import errno

with open("output.txt", "w") as d, open("input.txt", "r") as f, open("error.txt", "w")as g:
    print("ipaddress, hostname", file=d)
    ipaddy = f.read()
    #print(ipaddy.split())
    for host in ipaddy.split():
        try:
            sep = '/'
            sep1 = ':'
            if "://" in host:
                host = host[host.index("://")+3:]
            if ":" in host:
                host = host[:host.index(":")]
            if "/" in host:
                host = host[:host.index("/")]
            """ 
            s = host.strip().strip("http://")
            x = s.split(sep)[0]
            y = x.split(sep1)[0]
            """
            j = socket.gethostbyname(host)
            print(",".join([j, host]), file=d)
        except Exception as e:
            print(host, file=g)
            print(e, file=g)
