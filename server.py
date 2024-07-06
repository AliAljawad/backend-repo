import yaml
import os

class Server:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '../config.yaml')
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
            self.server_ip = config.get('ServerIPAddress', 'localhost')

    def start(self):
        print(f"Server starting at {self.server_ip}")

if __name__ == "__main__":
    server = Server()
    server.start()
