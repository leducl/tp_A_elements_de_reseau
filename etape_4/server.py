import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(1)
print("Serveur en attente de connexion...")

conn, addr = serveur.accept()
print("Client connecté:", addr)

while True:
    message = conn.recv(1024).decode()
    if message.lower() == "fin":
        break
    print("Client dit:", message)
    reponse = input("Répondre > ")
    conn.send(reponse.encode())

conn.close()
serveur.close()
