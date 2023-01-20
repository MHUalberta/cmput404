#The code used in this program is from the CMPUT404 labs, both the lab session on the 16th of January 2023
#and some of the provided old lab videos on the course eclass page.

import socket

HOST = "localhost"
PORT = 8101
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: www.google.com\r\n\r\n"

def connect(addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #IPv4, TCP
        s.connect(addr)
        s.sendall(payload.encode())
        s.shutdown(socket.SHUT_WR)

        full_data = s.recv(BUFFER_SIZE)
        print(full_data)
    
    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    connect(('127.0.0.1', PORT))

if __name__ == "__main__":
    main()

