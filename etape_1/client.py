import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.20.90", 63000))

client.send("Bonjour serveur !".encode())
message = client.recv(1024).decode()
print("Message reçu:", message)

client.close()
