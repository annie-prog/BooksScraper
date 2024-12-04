import socket
from threading import Thread

def scraper_task(task_id):
    print(f"Executing task {task_id}...")

def handle_client(conn):
    try:
        data = conn.recv(1024).decode()
        if not data:
            return
        num_threads = int(data)
        print(f"Received number of threads: {num_threads}")

        threads = []
        for i in range(num_threads):
            thread = Thread(target=scraper_task, args=(i,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        conn.send("Scraper tasks completed!".encode())
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 8080))
    server.listen(5)
    print("Server listening on port 8080...")

    while True:
        conn, addr = server.accept()
        print(f"Connected by {addr}")
        Thread(target=handle_client, args=(conn,)).start()

if __name__ == "__main__":
    start_server()