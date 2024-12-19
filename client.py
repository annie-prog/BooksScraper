import json
import socket
import sys

def run_client():

    """
    Client application for retrieving lines of data from the server.
    """

    if len(sys.argv) < 2:
        print("Error: No arguments provided. Usage: python client.py <args>")
        return

    client_args = sys.argv[1:]
    serialized_args = json.dumps(client_args, ensure_ascii=False)

    requested_lines = input("Enter the number of lines to retrieve from the server: ")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(("localhost", 8080))

        serialized_size = len(serialized_args)
        client_socket.sendall(str(serialized_size).encode("utf-8"))

        acknowledgment = client_socket.recv(1024).decode("utf-8")
        if acknowledgment != "SIZE_RECEIVED":
            print("Error: Server did not acknowledge size.")
            return

        client_socket.sendall(serialized_args.encode("utf-8"))
        client_socket.sendall(requested_lines.encode("utf-8"))

        server_response = b""
        while True:
            data_chunk = client_socket.recv(4096)
            if not data_chunk:
                break
            server_response += data_chunk

        received_data = json.loads(server_response.decode("utf-8"))
        print("Received from server:")
        for line in received_data:
            print(line.strip())

if __name__ == "__main__":
    run_client()