import socket

#consider adding argument paramerters for file input and output
with open("output.txt", "w") as d, open("input.txt", "r") as f, open("output_error.txt", "w")as g:
    print("ipaddress, hostname, alias", file=d)
    print("ipaddress, errormsg", file=g)
    ipaddy = f.read()


    for host in ipaddy.split('\n'):
        try:
            j = socket.gethostbyaddr(host)
            ip = j[2]
            host = j[0]
            alias = j[1]
            for i in ip:
                print(i)

            print("{}, {}{}".format(i, host, ", " + ", ".join(alias) if alias else ", none"), file=d)
        except Exception as e:
            print(f"{i}, {e}", file=g)
