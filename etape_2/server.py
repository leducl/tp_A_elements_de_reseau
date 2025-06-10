import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(1)
print("Serveur en attente de connexion...")
conn, addr = serveur.accept()
print("Client connecté:", addr)

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == "fin":
        break
    print("Message reçu:", msg)
    conn.send(msg.encode())

conn.close()
serveur.close()
