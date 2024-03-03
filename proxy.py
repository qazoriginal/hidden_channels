import socket
import datetime

def receive_packet(server_socket):
    data, addr = server_socket.recvfrom(8)
    return data

def read_udp_packets(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    cur = 1.0
    delta = 4.0
    accuracy = 2.0
    read = 0
    info = b''
    try:
        while True:
            if read == 0:
                cur = 1.0
                data = receive_packet(server_socket)
                data = receive_packet(server_socket)
                data = receive_packet(server_socket)
                print('Start decoding')
            timestamp = datetime.datetime.now().timestamp()
            data = receive_packet(server_socket)
            if datetime.datetime.now().timestamp() - timestamp > cur + accuracy:
                cur += delta
                print('1 was taken')
                info += b'1'
                read += 1
            else:
                print('0 was taken')
                info += b'0'
                read += 1
            if read == 8:
                read = 0
                print('Decoded info: ')
                print(info)
                data = receive_packet(server_socket)
                data = receive_packet(server_socket)
                data = receive_packet(server_socket)
                info = b''

    except KeyboardInterrupt:
        print("Прервано пользователем")
    finally:
        server_socket.close()

if __name__ == "__main__":
    host = '10.111.0.1'
    port = 12345
    read_udp_packets(host, port)
