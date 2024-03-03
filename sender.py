import socket
import time
import random

def send_packet(host, port, packet_length):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_data = b''
    for i in range(0, packet_length):
        if random.choice([0, 1]) == 1:
            packet_data += b'1'
        else:
            packet_data += b'0'
    print(packet_data)
    print(b'0' * 8)
    client_socket.sendto(packet_data, (host, port))
    client_socket.close()
if __name__ == "__main__":
    server_host = '10.111.0.10'
    server_port = 12344
    packet_length = 8
    try:
        while True:
            send_packet(server_host, server_port, packet_length)
            time.sleep(random.uniform(1.0, 3.0))
    except KeyboardInterrupt:
        print("Прервано пользователем")
