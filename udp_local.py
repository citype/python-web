import argparse, socket
from datetime import datetime

MAX_BYTES = 65535

def server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',port))
    print('Listening at {}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('ascii')
        # 接受到消息设备地址 以及消息内容
        print('The client at {} syas {!r}'.format(address,text))
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)


def clien(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = 'The time is {}'.format(datetime.now())
    data = text.encode('ascii')
    # sendto 要发送的信息 以及地址
    sock.sendto(data, ('127.0.0.1',port))
    print('The OS assgined me the address {}'.format(sock.getsockname))
    # Danger! 没有检查数据报的源地址，也没有验证数据报是否确实是服务器发回的响应
    data, address = sock.recvfrom(MAX_BYTES) 
    text = data.decode('ascii')
    print('The serve {} replied {!r}'.format(address, text))

if __name__ == '__main__' :
    choices = {'client':clien,'server':server}
    parser = argparse.ArgumentParser(description = 'Seng and recive UDP locally')
    parser.add_argument('role', choices = choices, help = 'which role to play')
    parser.add_argument('-p', metavar = 'PORT', type = int, default = 1060, 
                        help = 'UDP port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
    