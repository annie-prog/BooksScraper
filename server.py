import json
from module.modules.argument_parser import ArgumentParser
from module.modules.book_scraper import BookScraper
import socket

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 8080))
        s.listen(5)
        print("Server listening on port 8080...")

        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")

            size_data = conn.recv(1024).decode('utf-8')
            try:
                data_size = int(size_data)
                conn.sendall(b"SIZE_RECEIVED")
            except ValueError:
                print("Error: Invalid data size received.")
                conn.sendall(b"SIZE_ERROR")
                return

            received_data = b""
            while len(received_data) < data_size:
                chunk = conn.recv(4096)
                if not chunk:
                    break
                received_data += chunk
            
            try:
                input_arguments = json.loads(received_data.decode('utf-8'))
                print(f"Received input arguments: {input_arguments}")

                argument_parser = ArgumentParser()
                parsed_args = argument_parser.parser.parse_args(input_arguments)

                book_scraper = BookScraper(parsed_args)
                books_info = book_scraper.scrape_books()

                with open('data.json', 'r', encoding='utf-8') as f:
                    books_data = f.read()

                conn.sendall(books_data.encode('utf-8'))
                print("Books data sent to the client.")
            except Exception as e:
                conn.sendall(b"Error processing request.")

if __name__ == "__main__":
    start_server()