import socket
import ssl
import time

target_host = 'hostname'
http_port = 80
https_port = 443
version = ssl.create_default_context()

def httpRequest():
    print('-----BEGIN HTTP REQUEST-----')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        request = f'GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n'
        #print('*begin request traffic*')
        #print(repr(request))
        #print('*end request traffic*')
        s.connect((target_host, http_port))

        s.sendall(request.encode())
        data = s.recv(4096)
        print(data.decode())
        print('\n-----END OF HTTP REQUEST-----\n')
        time.sleep(2)

def httpsRequest():
    print('\n-----BEGIN HTTPS REQUEST-----\n')
    with socket.create_connection((target_host, https_port)) as sock:
        with version.wrap_socket(sock, server_hostname=target_host) as ssock:
            print('\nSSL Version: ', ssock.version(), '\n')

            request = f'GET / HTTP/1.1\r\nHost: {target_host}\r\n\r\n'
            #print('*begin request traffic*')
            #print(repr(request))
            #print('*end request traffic*')

            ssock.sendall(request.encode())
            data = ssock.recv(4096)
            print(data.decode())
            print('\n-----END OF HTTPS REQUEST-----\n')
            time.sleep(2)

httpsRequest()

