import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(1)
print("Serveur en attente de connexion...")
conn, addr = serveur.accept()
print("Client connecté:", addr)

message = conn.recv(1024).decode()
print("Message reçu:", message)
conn.send("Bonjour client !".encode())

conn.close()
serveur.close()
