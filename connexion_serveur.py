import socket
import threading

HOST = '192.168.1.12'
PORT = 5000
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients, names = [], []
serveur.bind((HOST, PORT))



def chat():
    """_summary_

    Args:
        client (_type_): _description_
        addr (_type_): _description_
    """
    
    print("The serveur is starting")
    serveur.listen()
    while True:
        conn, addr = serveur.accept()
        conn.send("NAME".encode("utf-8"))
        name = conn.recv(1024).decode("utf-8")
        names.append(name)
        clients.append(addr)
        broadcast(f"{name} a rejoint le chat !".encode("utf-8"))     
        conn.send("Connection réussie !".encode("utf-8"))
        thread = threading.Thread(target = handle, args = (conn, addr))
        thread.start()


def handle(conn, addr):
    print("Nouvelle connexion ",addr)
    connected = True
    while connected:
        msg = conn.recv(1024)
        broadcast(msg)
    conn.close()
    

def broadcast(msg):
    for client in clients:
        client.send(msg)
        
chat()