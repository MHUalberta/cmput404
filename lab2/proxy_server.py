#The code used in this program is from the CMPUT404 labs, both the lab session on the 16th of January 2023
#and some of the provided old lab videos on the course eclass page.

#!/usr/bin/env python3
import socket
import sys
from multiprocessing import Process

#define address & buffer size
HOST = ""
PORT = 8101
BUFFER_SIZE = 1024

def get_remote_ip(host):
    print(f'Getting IP for {host}')
    try:
        remote_ip = socket.gethostbyname(host)
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
    
    print(f'IP address of {host} is {remote_ip}')
    return remote_ip


def main():
    host = "www.google.com"
    port = 80

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_start:
        print("Starting proxy server")
        proxy_start.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        proxy_start.bind((HOST, PORT))
        proxy_start.listen(1)

        while True:
            conn, addr = proxy_start.accept()
            print("Connected by", addr)

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("Connecting to Google")
                remote_ip = get_remote_ip(host)

                proxy_end.connect((remote_ip, port))

                p = Process(target = handle_request, args = (conn, proxy_end))
                p.daemon = True
                p.start()
                print("Started process", p)
            
            conn.close()


def handle_request(conn, proxy_end):
    send_full_data = conn.recv(BUFFER_SIZE)
    print(f"Sending recieved data {send_full_data} to google")
    proxy_end.sendall(send_full_data)

    proxy_end.shutdown(socket.SHUT_WR)

    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending recieved data {data}")
    conn.send(data)
    

if __name__ == "__main__":
    main()