import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(1)
print("Serveur avec protocole en attente...")

conn, addr = serveur.accept()
print("Client connecté:", addr)
pseudo = "Client"  # Par défaut

while True:
    message = conn.recv(1024).decode()
    if not message:
        break
    
    if message.startswith('/'):
        parts = message.split(' ', 1)
        commande = parts[0]
        contenu = parts[1] if len(parts) > 1 else ""
        
        if commande == '/pseudo':
            pseudo = contenu
            reponse = f"Pseudo changé pour {pseudo}"
        elif commande == '/me':
            reponse = f"* {pseudo} {contenu}"
        elif commande == '/all':
            reponse = f"[{pseudo}] {contenu}"
        elif commande == '/bye':
            reponse = f"À bientôt {pseudo} !"
            conn.send(reponse.encode())
            break
        elif commande == '/help':
            reponse = "Commandes: /pseudo, /me, /all, /bye, /help"
        else:
            reponse = "Commande inconnue"
    else:
        reponse = f"[{pseudo}] {message}"
    
    conn.send(reponse.encode())

conn.close()
serveur.close()
