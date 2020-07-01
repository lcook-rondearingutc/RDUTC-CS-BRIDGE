import socket

def main():
    port = getport()
    ip = getip()
    bindhp = (ip, port)
    Server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    join = str("/join" + socket.gethostbyname(socket.gethostname())).encode('utf-8')
    Server.sendto(join, bindhp)
    while True:
        print("\"/leave\" to leave")
        message = input(">>> ")
        if message == "/leave":
            leave = str("/leave" + socket.gethostbyname(socket.gethostname())).encode('utf-8')
            Server.sendto(leave, bindhp)
            break
        else:
            message = str(socket.gethostbyname(socket.gethostname()) + ": " + message).encode('utf-8')
            Server.sendto(message, bindhp)
    Server.close()

def getport():
    file_port = open("server-port.ini", "r")
    port = int(file_port.read())
    file_port.close()
    return port

def getip():
    file_ip = open("server-ip.ini", "r")
    ip = str(file_ip.read())
    file_ip.close()
    return ip

if __name__ == "__main__":
    main()
