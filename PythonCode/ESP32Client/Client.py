import socket 
import json
class Client:
    def __init__(self,ESPIP:str,port:int):
        self.ESPIP = ESPIP
        self.port=  port

    def connect(self):
        #establish connection with server
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            print("Waiting to Connect...\n")
            self._sock.connect((self.ESPIP, self.port)) 
            print("Connection Established!\n")
            
        except socket.error as e:
            print(f"Failed to connect :( \n{e}")

    def close(self):
        self._sock.close()
        print("Connection Closed...")

    def send(self,data:dict):
        json_data = json.dumps(data)
        self._sock.sendto(json_data.encode(), (self.ESPIP, self.port))
