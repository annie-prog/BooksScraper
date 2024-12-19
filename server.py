import json
import socket
from module.modules.argument_parser import ArgumentParser
from module.modules.book_scraper import BookScraper


def start_server():

    """
    Starts the server to handle client requests and serve data.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(("localhost", 8080))
        server_socket.listen(5)
        print("Server listening on port 8080...")

        client_connection, client_address = server_socket.accept()
        with client_connection:
            print(f"Connected by {client_address}")

            size_data = client_connection.recv(1024).decode("utf-8")
            try:
                data_size = int(size_data)
                client_connection.sendall(b"SIZE_RECEIVED")
            except ValueError:
                print("Error: Invalid data size received.")
                client_connection.sendall(b"SIZE_ERROR")
                return

            received_data = b""
            while len(received_data) < data_size:
                data_chunk = client_connection.recv(4096)
                if not data_chunk:
                    break
                received_data += data_chunk

            try:
                input_arguments = json.loads(received_data.decode("utf-8"))
                print(f"Received input arguments: {input_arguments}")

                argument_parser = ArgumentParser()
                parsed_arguments = argument_parser.parser.parse_args(input_arguments)

                book_scraper = BookScraper(parsed_arguments)
                scraped_books = book_scraper.scrape_books()

                requested_lines = client_connection.recv(1024).decode("utf-8")
                requested_lines = int(requested_lines)
                print(f"Number of lines requested: {requested_lines}")

                with open("data.json", "r", encoding="utf-8") as data_file:
                    all_books_data = data_file.readlines()

                limited_data = all_books_data[:requested_lines]
                response = json.dumps(limited_data, ensure_ascii=False)

                client_connection.sendall(response.encode("utf-8"))
                print("Books data sent to the client.")
            except Exception as error:
                print(f"Error: {error}")
                client_connection.sendall(b"Error processing request.")

if __name__ == "__main__":
    start_server()