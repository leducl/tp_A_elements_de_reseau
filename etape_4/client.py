import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("172.16.21.90", 63000))

while True:
    message = input("Votre message (ou 'fin' pour terminer): ")
    client.send(message.encode())
    if message.lower() == "fin":
        break
    reponse = client.recv(1024).decode()
    print("Serveur dit:", reponse)

client.close()
