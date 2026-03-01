import sys
from PyQt6.QtWidgets import QApplication

from monitor_window import MonitorWindow


def main():
    app = QApplication(sys.argv)
    window = MonitorWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()