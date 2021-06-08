import socket
    
host="192.168.188.24"
port=654

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(b"I am the best")
    data=sock.recv(100)
    print(data.decode("ascii"))
    print("Sending next data...")
    sock.sendall(b"tseb eht ma I")
    data=sock.recv(100)
    print("Result:", data.decode("ascii"))