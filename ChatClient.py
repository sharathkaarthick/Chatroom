import socket 
import threading 

PORT = 5555
SERVER = "127.0.0.1" 
ADDRESS = (SERVER, PORT) 
FORMAT = "utf-8"

client = socket.socket(socket.AF_INET,  socket.SOCK_STREAM) 
client.connect(("127.0.0.1",PORT)) 
nickname=input("Your Name : ")

def receive():
     while True:
         try:
             msg=client.recv(1024).decode("utf-8")
             if msg == "NAME":
                 client.send(nickname.encode("utf-8"))
             else:
                 print(msg,"\n")
         except:
            print("Error...")
            client.close()
            break
def sendmsg():
    while True:
        msg=f' {nickname} : {input("")} '
        client.send(msg.encode("utf-8"))

receive_Thread=threading.Thread(target=receive)
receive_Thread.start()

sendmsg_Thread=threading.Thread(target=sendmsg)
sendmsg_Thread.start()