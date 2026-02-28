# Moniteur Système - Pattern Façade

Une application de monitoring système développée en Python avec PyQt6. 
Ce projet illustre l'implémentation du Design Pattern Façade pour séparer une interface graphique d'un sous-système.

## Architecture du Projet

L'application est divisée en deux parties distinctes :
* Le Client (`main.py` & `monitor_window.py`) : Gère uniquement l'affichage et les interactions utilisateur.
* Le Sous-système (`/core`) : Contient la logique d'analyse (CPU, Réseau, Disque). Toute cette complexité est masquée derrière le point d'entrée unique `system_monitor_facade.py`.

## Prérequis

Assurez-vous d'avoir Python 3.x installé sur votre machine, puis installez les dépendances graphiques :

```bash
pip install PyQt6
```

## Comment lancer l'application

1. Ouvrez un terminal (ou une invite de commande) dans le dossier de ce projet.
2. Tapez simplement cette commande :

```bash
python main.py
```