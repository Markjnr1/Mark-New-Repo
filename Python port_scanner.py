ALLOWED_HOSTS = {"127.0.0.1", "localhost", "scanme.nmap.org"}

import socket
import time

def scan_ports(host, start_port, end_port, delay=0.05):
    """Scan a range of ports on an approved host."""
    if host not in ALLOWED_HOSTS:
        print("[ERROR] Unauthorized host. Only scan 127.0.0.1, localhost, or scanme.nmap.org")
        return

    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print("[ERROR] Port numbers must be between 1 and 65535.")
        return

    if start_port > end_port:
        print("[ERROR] Start port must be less than or equal to end port.")
        return

    try:
        target_ip = socket.gethostbyname(host)
        print(f"\nScanning host: {host} ({target_ip})")
        print(f"Port range: {start_port}-{end_port}\n")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            try:
                result = sock.connect_ex((target_ip, port))
                if result == 0:
                    print(f"Port {port}: OPEN")
                else:
                    print(f"Port {port}: CLOSED")
            except socket.gaierror:
                print("[ERROR] Hostname could not be resolved.")
                break
            except socket.error as e:
                print(f"[ERROR] Could not connect to port {port}: {e}")
            finally:
                sock.close()

            time.sleep(delay)

    except socket.gaierror:
        print("[ERROR] Invalid or unreachable host.")
    except Exception as e:
        print(f"[SCANNER ERROR] {e}")

def main():
    print("Authorized hosts only: 127.0.0.1, localhost, scanme.nmap.org")
    host = input("Enter target host: ").strip()

    try:
        start_port = int(input("Enter start port: ").strip())
        end_port = int(input("Enter end port: ").strip())
        scan_ports(host, start_port, end_port)
    except ValueError:
        print("[ERROR] Please enter valid numeric port values.")

if __name__ == "__main__":
    main()