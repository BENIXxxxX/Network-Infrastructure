import socket

def find_service_name():
    ports = [80, 25, 22, 990]
    for port in ports:
        print(f"Port: {port} >> service Name: "
                f"{socket.getservbyport(port, 'tcp')}")

if __name__ == "__main__":
    find_service_name()