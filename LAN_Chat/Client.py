import socket

def main():
    port = getport()
    print("Client IP: " + socket.gethostbyname(socket.gethostname()))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bindhp = ("", port)
    client.bind(bindhp)
    while True:
        recieve, location = client.recvfrom(10000)
        recieve = recieve.decode('utf-8')
        print(recieve)

def getport():
    file_port = open("client-port.ini", "r")
    port = int(file_port.read())
    file_port.close()
    return port

if __name__ == "__main__":
    main()
