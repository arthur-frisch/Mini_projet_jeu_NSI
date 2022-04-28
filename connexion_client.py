import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '192.168.1.12'
PORT = 5000
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                print(msg.decode())
            else:
                client.close()
                break
        except Exception as error:
            print("Erreur : ", error)
            client.close()
            break
     
threading.Thread(target=receive)
print("Connecté !")   
while True:
    msg = ("Me : ")
    if msg == "quit":
        break
    client.send(msg.encode("utf-8"))
client.close()


        
        

    
    