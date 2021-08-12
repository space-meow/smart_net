import argparse
import socket

from lib.message_consts import *
from lib.client_actions import (
    set_alarm,
    set_timer
)
from lib.client_utils import construct_msg

def show_menu():
    choice = None
    while choice not in ALL_MESSAGES:
        for msg in ALL_MESSAGES:
            print(msg)
        choice = str(input("Choice: ").lower())
    return choice



def run_client(ip):
    while True:
        # open socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, 1579))

        # get welcome from smart_net server
        msg = s.recv(1024)
        print(msg.decode("utf-8"))

        # pick action choice and send
        choice = show_menu()
        print(choice)
        if choice == SET_ALARM: args = set_alarm()
        elif choice == SET_TIMER: args = set_timer()
        print(args)
        msg = construct_msg(choice, args)
        s.sendall(bytes(msg, "utf-8"))

        # close the connection
        s.close()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-ip", "--ip-address", dest="ip", required=True)
    args = parser.parse_args()

    run_client(args.ip)
