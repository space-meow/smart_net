import argparse
import socket


def run_client(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, 1579))

    msg = s.recv(1024)
    print(msg.decode("utf-8"))
    s.sendall(bytes("Sending message back", "utf-8"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip-address", dest="ip", required=True)
    args = parser.parse_args()

    run_client(args.ip)
