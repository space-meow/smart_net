
import argparse
import socket


def start_server(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, 1579))
    s.listen(5)


    while True:
        clientsocket, address = s.accept()
        print(f"Connection from {address} has been established!")
        clientsocket.send(bytes("Welcome to the server!", "utf-8"))
        print(clientsocket.recv(1024).decode("utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip-address", dest="ip", required=True)
    args = parser.parse_args()

    start_server(args.ip)
