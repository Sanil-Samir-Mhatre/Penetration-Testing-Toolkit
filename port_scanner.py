import socket


class PortScanner:
    def __init__(self, host, start_port, end_port):
        self.host = host
        self.start_port = start_port
        self.end_port = end_port

    def scan(self):
        print(f"Scanning {self.host} from port {self.start_port} to {self.end_port}...")
        for port in range(self.start_port, self.end_port + 1):
            self.check_port(port)

    def check_port(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((self.host, port)) == 0:
                print(f"[+] Port {port} is open")
