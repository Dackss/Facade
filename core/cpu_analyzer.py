# Utilisation de la bibliothèque os pour interagir avec l'os
# Doc : https://docs.python.org/3/library/os.html
import os

# Classe pour récupérer les informations du processeur
class CPUAnalyzer:

    # Récupère le nombre de cœurs du processeur
    @staticmethod
    def get_core_count() -> int:
        return os.cpu_count()