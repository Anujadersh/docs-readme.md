import socket
import threading

target = input("Enter target IP or domain: ")

print(f"\nScanning target: {target}\n")

def scan_port(port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = scanner.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} is OPEN")
    
    scanner.close()

threads = []

for port in range(1, 101):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("\nScan completed!")
