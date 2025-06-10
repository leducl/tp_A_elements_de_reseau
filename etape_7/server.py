import socket
import threading

def gerer_client(conn, addr):
    print("Nouvelle connexion:", addr)
    try:
        while True:
            msg = conn.recv(1024).decode()
            if not msg or msg.lower() == "fin":
                break
            print(f"[{addr}] dit:", msg)
            conn.send(msg.encode())
    finally:
        conn.close()
        print("Déconnexion de", addr)

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(5)
print("Serveur multi-threadé en attente...")

while True:
    conn, addr = serveur.accept()
    thread = threading.Thread(target=gerer_client, args=(conn, addr))
    thread.start()
