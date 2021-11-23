from enum import Enum
from socket import *

SERVER_IP = '134.103.206.222'
SERVER_PORT = 12069

# This Enum data type stores the commands from the GUI that is to be transmitted to the server
class GUICommands(Enum):
    CP_FREE_ROAMING = "CP_FREE_ROAMING"
    CP_FOLLOW_LEFT_WALL = "CP_FOLLOW_LEFT_WALL"
    CP_FOLLOW_RIGHT_WALL = "CP_FOLLOW_RIGHT_WALL"
    CP_USER_CONTROL = "CP_USER_CONTROL"
    BP_FORWARD = "BP_FORWARD"
    BP_BACK = "BP_BACK"
    BP_LEFT = "BP_LEFT"
    BP_RIGHT = "BP_RIGHT"
    BP_STOP = "BP_STOP"

# We setup the GUI as a client - it will initiate the communication with the server which runs on the GoPiGo
class Client():
    def __init__(self):
        self.server_ip = SERVER_IP
        self.server_port = SERVER_PORT
        self.client_socket = None

    def connect(self):
        print(" Connecting to the server...")
        self.client_socket = socket(AF_INET, SOCK_DGRAM)
        print(" Connected to the server...")
        message = 'connected'
        self.client_socket.sendto(message.encode(), (self.server_ip, self.server_port))
        print("message sent")
        modified_message,server_address = self.client_socket.recvfrom(2048)
        print(modified_message.decode())

        print(" Finished...")

    def close_connection(self):
        self.client_socket.close()

    def receive_message(self):
        message, client_address = self.client_socket.recvfrom(2048)
        modified_message = message.decode()
        return modified_message

    def send_message(self, message):
        self.client_socket.sendto(message.encode(), (self.server_ip, self.server_port))