import socket
    
host="192.168.188.24"
port=8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.sendall(b"Get this for me!\nGET /sample-greeting.html http/1.1\nI wanna see!")
    data=sock.recv(1000)
    print(data.decode("ascii"))