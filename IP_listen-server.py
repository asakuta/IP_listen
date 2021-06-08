import socket
    
host="0.0.0.0"
port=654

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    while True:
        (con, add)=sock.accept()
        with con:
            print("Connected by: ", add)
            data1=con.recv(100)
            if not data1:
                break
            word1=data1.decode("ascii")
            print("First data: ", word1)
            con.sendall(b"Data sent")
            data2=con.recv(100)
            if not data2:
                break
            word2=data2.decode("ascii")
            print("Second data: ", word2)
            target=word1.lower()[::-1]
            print("Evaluating...")
            result=""
            if word2.lower() == target:
                result=b"Success"
            else:
                result=b"Failure"
            print(result.decode("ascii"))
            con.sendall(result)
            
