from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QTextEdit, QLabel, QGroupBox, QFormLayout)
from PyQt6.QtGui import QFont, QCursor
from PyQt6.QtCore import Qt

from core.system_monitor_facade import SystemMonitorFacade


class MonitorWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        # Configuration de base de la fenêtre
        self._setup_window()

        # Création des composants de l'interface
        self._create_widgets()
        self._create_layouts()

        # Instanciation de la Façade
        self.__facade: SystemMonitorFacade = SystemMonitorFacade(self.log_to_console)
        self.__btn_scan.clicked.connect(self.run_scan)

    # Config les propriétés globales de la fenêtre
    def _setup_window(self) -> None:
        self.setWindowTitle("Moniteur Système")
        self.resize(480, 450)
        self.setStyleSheet("background-color: #f5f6fa; color: #2c3e50;")

    # Sert à instancier tous les widgets de la fenêtre
    def _create_widgets(self) -> None:
        self.__btn_scan = QPushButton("Lancer l'analyse système")
        self.__btn_scan.setStyleSheet("""
            QPushButton { background-color: #3498db; color: white; padding: 10px; font-weight: bold; font-size: 13px; border-radius: 5px; }
            QPushButton:hover { background-color: #2980b9; }
            QPushButton:disabled { background-color: #bdc3c7; color: #7f8c8d; }
        """)
        self.__btn_scan.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        # Label d'attente pour les données
        self.__lbl_cores = QLabel("En attente...")
        self.__lbl_hostname = QLabel("En attente...")
        self.__lbl_ip = QLabel("En attente...")
        self.__lbl_disk = QLabel("En attente...")

        # Application des styles spécifiques
        self.__lbl_cores.setStyleSheet("color: #e74c3c; font-weight: bold; font-size: 14px; background: transparent;")
        self.__lbl_disk.setStyleSheet("color: #27ae60; font-weight: bold; font-size: 14px; background: transparent;")
        for lbl in [self.__lbl_hostname, self.__lbl_ip]:
            lbl.setStyleSheet("color: #3498db; font-weight: bold; background: transparent;")

        # Console de log
        self.__text_console = QTextEdit()
        self.__text_console.setReadOnly(True)
        self.__text_console.setMinimumHeight(150)
        self.__text_console.setFont(QFont("Consolas", 9))
        self.__text_console.setStyleSheet("background-color: white; color: #576574; border: 1px solid #dcdde1; border-radius: 5px; padding: 4px;")

    # Sert à organiser tous les widgets dans la fenêtre
    def _create_layouts(self) -> None:
        # Styles pour les cartes
        card_style = "QGroupBox { background-color: white; border: 1px solid #dcdde1; border-radius: 6px; margin-top: 10px; } QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #7f8fa6; font-weight: bold; }"

        # Création des différentes cartes
        group_cpu = QGroupBox("Processeur")
        group_cpu.setStyleSheet(card_style)
        layout_cpu = QVBoxLayout()
        layout_cpu.setContentsMargins(10, 15, 10, 10)
        self.__lbl_cores.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_cpu.addWidget(self.__lbl_cores)
        group_cpu.setLayout(layout_cpu)

        group_net = QGroupBox("Réseau")
        group_net.setStyleSheet(card_style)
        layout_net = QFormLayout()
        layout_net.setContentsMargins(10, 15, 10, 10)
        layout_net.addRow("Hôte :", self.__lbl_hostname)
        layout_net.addRow("IP :", self.__lbl_ip)
        group_net.setLayout(layout_net)

        group_disk = QGroupBox("Stockage (Disque Principal)")
        group_disk.setStyleSheet(card_style)
        layout_disk = QVBoxLayout()
        layout_disk.setContentsMargins(10, 15, 10, 10)
        self.__lbl_disk.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout_disk.addWidget(self.__lbl_disk)
        group_disk.setLayout(layout_disk)

        # Grille centrale
        cards_layout = QGridLayout()
        cards_layout.setSpacing(10)
        cards_layout.addWidget(group_cpu, 0, 0)
        cards_layout.addWidget(group_net, 0, 1)
        cards_layout.addWidget(group_disk, 1, 0, 1, 2)

        # Zone de la console de log
        log_layout = QVBoxLayout()
        log_layout.setSpacing(2)
        lbl_log = QLabel("Journal d'activité :")
        lbl_log.setStyleSheet("color: #7f8fa6; font-size: 11px;")
        log_layout.addWidget(lbl_log)
        log_layout.addWidget(self.__text_console)

        # Assemblage final
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)
        main_layout.addWidget(self.__btn_scan)
        main_layout.addLayout(cards_layout)
        main_layout.addLayout(log_layout)
        self.setLayout(main_layout)

    # Affiche les messages dans la console et force le défilement vers le bas
    def log_to_console(self, message: str) -> None:
        self.__text_console.append(message)
        scrollbar = self.__text_console.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())
        QApplication.processEvents()

    # Fonction principale où on va appeler la façade et afficher les données
    def run_scan(self) -> None:
        self.__btn_scan.setEnabled(False)
        self.__btn_scan.setText("Analyse en cours...")
        self.__text_console.clear()

        # Appel de la Façade
        data = self.__facade.generate_report()

        # Mise à jour de l'UI
        self.__lbl_hostname.setText(data.hostname)
        self.__lbl_ip.setText(data.ip)
        self.__lbl_cores.setText(f"{data.cores} cœurs")
        self.__lbl_disk.setText(f"{data.disk_gb} Go libres")

        self.__btn_scan.setText("Lancer l'analyse système")
        self.__btn_scan.setEnabled(True)