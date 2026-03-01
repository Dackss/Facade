from dataclasses import dataclass


# @dataclass génère automatiquement le constructeur __init__ en arrière-plan
# Cette classe sert de structure fixe pour regrouper et transporter les résultats de l'analyse.
@dataclass
class ReportData:
    cores: int
    hostname: str
    ip: str
    disk_gb: float
