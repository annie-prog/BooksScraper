import json
import socket
import sys

def client_app():
    if len(sys.argv) < 2:
        print("Error: No arguments provided. Usage: python client.py <args>")
        return

    args = sys.argv[1:]

    args_json = json.dumps(args, ensure_ascii=False)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 8080))

        data_size = len(args_json)
        s.sendall(str(data_size).encode('utf-8'))

        ack = s.recv(1024).decode('utf-8')
        if ack != "SIZE_RECEIVED":
            print("Error: Server did not acknowledge size.")
            return

        s.sendall(args_json.encode('utf-8'))

        with open('data.json', 'r', encoding='utf-8') as f:
            books_data = f.read()
        
        data_size = len(books_data)

        response = s.recv(data_size).decode('utf-8')
        print(f"Received from server: {response}")

if __name__ == "__main__":
    client_app()