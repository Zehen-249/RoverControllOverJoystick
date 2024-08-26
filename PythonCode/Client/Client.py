import socket 

class Client:
    def __init__(self,serverIp:str,port:int):
        self.serverIp = serverIp 
        self.port=  port

    def connect(self):
        #establish connection with server
        try:
            self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print("Waiting to Connect...\n")
            self._sock.connect((self.serverIp, self.port)) 
            print("Connection Established!\n")
        except socket.error as e:
            print(f"Failed to connect :( \n{e}")

    def close(self):
        self._sock.close()
        print("Connection Closed...")

    def send(self,data:str):
        self._sock.sendall(data.encode())
