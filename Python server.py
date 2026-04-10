import socket

HOST = "127.0.0.1"
PORT = 65432

def start_server():
    """Start a simple server that accepts one client at a time."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[SERVER] Listening on {HOST}:{PORT}...")

        conn, addr = server_socket.accept()
        print(f"[SERVER] Connected by {addr}")

        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    print("[SERVER] Client disconnected.")
                    break

                message = data.decode().strip()
                print(f"[CLIENT] {message}")

                if message.lower() == "bye":
                    reply = "Goodbye from server."
                    conn.sendall(reply.encode())
                    print("[SERVER] Closing connection.")
                    break

                reply = f"Server received: {message}"
                conn.sendall(reply.encode())

    except Exception as e:
        print(f"[SERVER ERROR] {e}")
    finally:
        server_socket.close()
        print("[SERVER] Server shut down.")

if __name__ == "__main__":
    start_server()
