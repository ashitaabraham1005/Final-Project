from PyQt6.QtWidgets import *
import sys
from gui import Gui


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Gui()
    window.setWindowTitle('Voting Menu')
    window.setGeometry(100, 100, 400, 230)
    window.show()
    sys.exit(app.exec())
