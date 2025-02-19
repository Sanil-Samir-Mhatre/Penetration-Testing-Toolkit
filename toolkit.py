import socket
import os


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


class SimpleBruteForcer:
    def __init__(self, file_path, username, password_list):
        self.file_path = file_path
        self.username = username
        self.password_list = password_list

    def run(self):
        if not os.path.isfile(self.password_list):
            print(f"[Error] Password file not found: {self.password_list}. Please check the path.")
            return

        with open(self.password_list, 'r') as file:
            for password in file:
                password = password.strip()
                if self.attempt_login(password):
                    print(f"[+] Successful login: {self.username}:{password}")
                    return
                else:
                    print(f"[~] Attempted: {password}")

    def attempt_login(self, password):
        if not os.path.isfile(self.file_path):
            print(f"[Error] Target file not found: {self.file_path}. Please check the path.")
            return False

        with open(self.file_path, 'r') as file:
            content = file.read()
            if password in content:
                print(f"[+] Password found: {password}")
                return True
        return False


def main():
    print("=== Penetration Testing Toolkit ===")
    print("1. Run Port Scanner")
    print("2. Run Simple Brute-Forcer")
    print("3. Exit")

    choice = input("Select an option (1/2/3): ")

    if choice == "1":
        host = input("Enter the target host (IP or domain): ")
        port_range = input("Enter the port range to scan (e.g., 1-1000): ")

        try:
            start_port, end_port = map(int, port_range.split("-"))
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
        except ValueError:
            print("[Error] Invalid port range! Use format 'start-end' with valid numbers.")
            return

        scanner = PortScanner(host, start_port, end_port)
        scanner.scan()

    elif choice == "2":
        file_path = input("Enter the path to the file to check against: ")
        username = input("Enter the username: ")
        password_list = input("Enter the path to the password file: ")

        brute_forcer = SimpleBruteForcer(file_path, username, password_list)
        brute_forcer.run()

    elif choice == "3":
        print("Exiting...")
        return

    else:
        print("[Error] Invalid option. Please try again.")
        main()


if __name__ == "__main__":
    main()
