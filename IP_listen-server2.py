import sys
import json
import socket
    
host="0.0.0.0"
port=8080

resource={}
if len(sys.argv) > 1:
    File=sys.argv[1]
    handle=open(File, "r")
    with handle:
        text=handle.read()
        resource=json.loads(text)
        
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
                handle2=open(location, "r")
                text2=""
                with handle2:
                    text2=handle2.read()
                    for key in resource:
                        text2=text2.replace(key, resource[key])
                    print(text2)
                length=str(len(text2))
                content="\nHTTP/1.0 200 OK\nContent-Type: text/html; charset=utf-8\nContent-Length: "+length+"\nConnection: close\n\n"+text2
            except:
                content="\nHTTP/1.0 500 Internal Server Error\nContent-Length: 0\nConnection: close"
            toSend=str.encode(content)
            con.sendall(toSend)
            
