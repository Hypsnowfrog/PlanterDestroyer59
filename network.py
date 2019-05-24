import socket


class Network:

    def __init__(self, ip="172.16.97.13", port=8001):
        self.ip = ip
        self.port = int(port)
        self.sock = self._connectTo()

    def _connectTo(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            return sock
        except:
            raise Exception("Unable to connect to this ip and port.")

    def receive(self):
        try:
            data, addr = self.sock.recvfrom(2048)

        except:  # Si la connection est morte
            # recreate the socket and reconnect
            self.sock = self._connectTo()
            data = self.sock.recv(2048)
        return data.decode()

    def send(self, data):
        data = data.encode()

        try:
            self.sock.sendto(data, (self.ip, self.port))

        except:  # Si la connection est morte
            # recreate the socket and reconnect
            self.sock = self._connectTo()
            self.sock.sendto(data, (self.ip, self.port))


#udp 172.16.97.13 port 8000 8001 8002? 8003? 8004? 8000?