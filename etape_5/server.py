import socket
import math

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(("0.0.0.0", 63000))
serveur.listen(1)
print("Serveur calculatrice en attente...")

conn, addr = serveur.accept()
print("Client connecté:", addr)

while True:
    expression = conn.recv(1024).decode()
    if expression.lower() == "fin":
        break
    
    try:
        # Sécurité: on n'utilise pas eval() directement
        # On vérifie que l'expression ne contient que des caractères autorisés
        if all(c in '0123456789+-*/. ()' for c in expression):
            result = str(eval(expression))
        else:
            result = "Erreur: Caractères non autorisés"
    except Exception as e:
        result = f"Erreur: {str(e)}"
    
    conn.send(result.encode())

conn.close()
serveur.close()
