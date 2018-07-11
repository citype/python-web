import socket
import sys

if __name__ == '__main__':
    hostname = sys.argv[1]
    addr = socket.gethostbyname(hostname)
    print('IP Address of {} is {}'.format(hostname,addr))