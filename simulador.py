MENFA_SIMULADOR/
│
├── simulador.py
├── motor_fisico.py
├── interfaz_cabina.py
│
├── assets/
│   └── logo_menfa.png
import sys
from PyQt6.QtWidgets import QApplication
from interfaz_cabina import CabinaPerforador

def main():

    app = QApplication(sys.argv)

    ventana = CabinaPerforador()
    ventana.show()
interfaz_cabina.py
motor_fisico.py
re
requisitos.txt
simulador.py
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
  
