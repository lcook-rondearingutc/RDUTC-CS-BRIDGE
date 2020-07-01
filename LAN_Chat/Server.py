import socket

class Client:
    clients = []
    @classmethod
    def send(cls, recieve, port):
        for client_ip in cls.clients:
            bindhp = (client_ip, port)
            Client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            Client.sendto(recieve.encode('utf-8'), bindhp)
            Client.close()
    @classmethod
    def new_client(cls, client):
        if client not in cls.clients:
            cls.clients.append(client)
    @classmethod
    def old_client(cls, client):
        cls.clients.remove(client)

def main():
    port = getport()
    cport = getcport()
    print("Server local IP: " + socket.gethostbyname(socket.gethostname()))
    Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bindhp = ("", port)
    Server.bind(bindhp)
    while True:
        recieve, location = Server.recvfrom(10000)
        recieve = recieve.decode('utf-8')
        if recieve == "/join":
            Client.new_client(location[0])
        elif recieve == "/leave":
            Client.old_client(location[0])
        else:
            print(recieve)
            Client.send(recieve, cport)

def getport():
    file_port = open("server-port.ini", "r")
    port = int(file_port.read())
    file_port.close()
    return port

def getcport():
    file_port = open("client-port.ini", "r")
    port = int(file_port.read())
    file_port.close()
    return port

if __name__ == "__main__":
    main()
