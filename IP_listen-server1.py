import socket
    
host="0.0.0.0"
port=8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen()
    while True:
        (con, add)=sock.accept()
        with con:
            print("Connected by: ", add)
            data=con.recv(1000)
            if not data:
                break
            data1=data.decode("ascii")
            position=data1.find("GET")
            tempData=""
            for x in range(position, len(data1)):
                if data1[x] is "\n":
                    break
                tempData=tempData+data1[x]
            elements=tempData.split(" ")
            fileName=elements[1]
            print("Reading: "+fileName)
            location="c:/Users/Aska/Dropbox/2014Chichester/Programming/Python/IP_listen/"+fileName
            content=""
            try:
                handle=open(location, "r")
                text=""
                with handle:
                    text=handle.read()
                print("Content: "+text)
                length=str(len(text))
                content="\nHTTP/1.0 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: "+length+"\nConnection: close\n\n"+text
            except:
                content="\nHTTP/1.0 500 Internal Server Error\nContent-Length: 0\nConnection: close"
            print("Sending: "+content)
            toSend=str.encode(content)
            con.sendall(toSend)
            
