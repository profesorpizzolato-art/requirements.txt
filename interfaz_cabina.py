from PyQt6.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt6.QtGui import QPixmap

from motor_fisico import MotorFisico


class CabinaPerforador(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Simulador Control de Pozos - MENFA IPCL")
        self.setGeometry(100, 100, 1200, 700)

        self.motor = MotorFisico(10.5, 8000)

        self.init_ui()

    def init_ui(self):

        widget = QWidget()
        layout_principal = QVBoxLayout()

        # LOGO MENFA
        logo = QLabel()
        pixmap = QPixmap("assets/logo_menfa.png")
        logo.setPixmap(pixmap)
        logo.setScaledContents(True)
        logo.setFixedHeight(80)

        layout_principal.addWidget(logo)

        # PANEL PARAMETROS
        self.label_profundidad = QLabel("Profundidad: 8000 ft")
        self.label_mud = QLabel("Mud Weight: 10.5 ppg")

        layout_principal.addWidget(self.label_profundidad)
        layout_principal.addWidget(self.label_mud)

        # BOTONES OPERACIONALES
        botones = QHBoxLayout()

        btn_stop = QPushButton("Stop Pumps")
        btn_bop = QPushButton("Close BOP")

        botones.addWidget(btn_stop)
        botones.addWidget(btn_bop)

        layout_principal.addLayout(botones)

        widget.setLayout(layout_principal)

        self.setCentralWidget(widget)
      
