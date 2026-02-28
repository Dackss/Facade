# Utilisation de la bibliothèque socket pour les interfaces réseau
# Doc : https://docs.python.org/3/library/socket.html
import socket

# Classe pour récupérer les informations réseau du pc
class NetworkAnalyzer:

    # Récupère le nom de la machine sur le réseau
    @staticmethod
    def get_hostname() -> str:
        return socket.gethostname()

    # Récupère l'adresse IP associée au nom de la machine
    @staticmethod
    def get_ip_address(hostname: str) -> str:
        try:
            return socket.gethostbyname(hostname)
        except socket.error:
            return "127.0.0.1"  # En cas d'erreur réseau