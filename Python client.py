import socket

HOST = "127.0.0.1"
PORT = 65432

def start_client():
    """Connect to the server and exchange messages."""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print(f"[CLIENT] Connected to server at {HOST}:{PORT}")

        while True:
            message = input("Enter message for server (type 'aye all correct' to quit): ").strip()
            if not message:
                print("[CLIENT] Empty message not sent.")
                continue

            client_socket.sendall(message.encode())
            response = client_socket.recv(1024).decode()
            print(f"[SERVER RESPONSE] {response}")

            if message.lower() == "bye":
                print("[CLIENT] Disconnecting from server.")
                break

    except ConnectionRefusedError:
        print("[CLIENT ERROR] Could not connect. Make sure the server is running.")
    except Exception as e:
        print(f"[CLIENT ERROR] {e}")
    finally:
        client_socket.close()
        print("[CLIENT] Client closed.")

if __name__ == "__main__":
    start_client()