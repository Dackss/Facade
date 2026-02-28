# Utilisation de la bibliothèque shutil pour accéder aux infos du système de fichiers
# Doc : https://docs.python.org/3/library/shutil.html
import shutil

# Classe pour vérifier l'état de l'espace de stockage du pc
class DiskAnalyzer:

    # Calcule l'espace libre sur une partition donnée (ex: "/" ou "C:\\") et le retourne en giga octets
    @staticmethod
    def get_free_space_gb(path: str) -> float:
        # disk_usage renvoie le tuple (total, used, free) en octets
        total, used, free = shutil.disk_usage(path)

        # Conversion d'octets en Gigaoctets (1 Go = 1024^3 octets)
        free_gb = free / (1024 ** 3)
        return round(free_gb, 2)