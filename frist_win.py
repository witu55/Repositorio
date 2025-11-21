
import PyQt5
import PyQt5.QtCore
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel)

class FormularioVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario")
        self.setGeometry(200, 200, 300, 150)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Aquí iría el formulario..."))
        self.setLayout(layout)

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal")
        self.setGeometry(100, 100, 400, 100)

        # Botones
        self.boton_cerrar = QPushButton("Cerrar")
        self.boton_formulario = QPushButton("Llenar formulario")
        self.boton_recordar = QPushButton("Recuérdamelo más tarde")

        # Conexiones
        self.boton_cerrar.clicked.connect(self.cerrar_aplicacion)
        self.boton_recordar.clicked.connect(self.cerrar_aplicacion)
        self.boton_formulario.clicked.connect(self.abrir_formulario)

        # Layout
        layout = QHBoxLayout()
        layout.addWidget(self.boton_cerrar)
        layout.addStretch()
        layout.addWidget(self.boton_formulario)
        layout.addStretch()
        layout.addWidget(self.boton_recordar)

        self.setLayout(layout)

    def cerrar_aplicacion(self):
        QApplication.quit()

    def abrir_formulario(self):
        self.formulario = FormularioVentana()
        self.formulario.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())


