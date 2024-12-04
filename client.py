import socket

def client_app():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 8080))

    num_threads = input("Enter the number of threads: ")
    client.send(num_threads.encode())

    response = client.recv(1024).decode()
    print(f"Server response: {response}")

    client.close()

if __name__ == "__main__":
    client_app()