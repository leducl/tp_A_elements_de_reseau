import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 63000))

while True:
    message = input("Votre message (ou 'fin' pour terminer): ")
    client.send(message.encode())
    if message.lower() == "fin":
        break
    reponse = client.recv(1024).decode()
    print("Réponse du serveur:", reponse)

client.close()
