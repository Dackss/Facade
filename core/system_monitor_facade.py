import time
from typing import Callable

from core.cpu_analyzer import CPUAnalyzer
from core.network_analyzer import NetworkAnalyzer
from core.disk_analyzer import DiskAnalyzer
from core.report_data import ReportData


class SystemMonitorFacade:
    def __init__(self, logger_callback: Callable) -> None:
        # Récupération de la fonction de log pour communiquer avec l'interface
        # Le type Callable indique que l'argument doit être une fonction
        self.__log: Callable = logger_callback

    # Fonction principale qui gère toute l'analyse et renvoie les données
    def generate_report(self) -> ReportData:
        self.__log("Début de l'analyse système...")
        time.sleep(0.5)

        # Récupération des données du processeur
        self.__log(" -> Analyse du processeur...")
        cores = CPUAnalyzer.get_core_count()
        time.sleep(0.5)

        # Récupération des informations réseau
        self.__log(" -> Analyse du réseau...")
        hostname = NetworkAnalyzer.get_hostname()
        ip = NetworkAnalyzer.get_ip_address(hostname)
        time.sleep(0.5)

        # Récupération de l'espace disque
        self.__log(" -> Analyse du disque...")
        disk_gb = DiskAnalyzer.get_free_space_gb("/")
        time.sleep(0.5)

        # Instanciation de l'objet contenant toutes les données
        self.__log(" -> Compilation des données  ...")
        data = ReportData(cores, hostname, ip, disk_gb)
        time.sleep(0.5)

        self.__log("Analyse terminée avec succès !\n")

        # Retourne les données formatées pour l'interface graphique
        return data