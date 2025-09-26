import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QRadioButton, QPushButton, QLabel, QMessageBox

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Formulario Calculadora")
        self.setGeometry(200, 200, 300, 200)

        # Layout principal
        layout = QVBoxLayout()

        # Cajas de texto
        self.num1 = QLineEdit(self)
        self.num1.setPlaceholderText("Ingrese primer número")
        self.num2 = QLineEdit(self)
        self.num2.setPlaceholderText("Ingrese segundo número")
        layout.addWidget(self.num1)
        layout.addWidget(self.num2)

        # RadioButtons
        self.suma = QRadioButton("Sumar (+)")
        self.resta = QRadioButton("Restar (-)")
        self.multi = QRadioButton("Multiplicar (*)")
        self.divi = QRadioButton("Dividir (/)")
        layout.addWidget(self.suma)
        layout.addWidget(self.resta)
        layout.addWidget(self.multi)
        layout.addWidget(self.divi)

        # Botón ejecutar
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_ejecutar.clicked.connect(self.operar)
        layout.addWidget(self.btn_ejecutar)

        # Botón salir
        self.btn_salir = QPushButton("Salir")
        self.btn_salir.clicked.connect(self.close)
        layout.addWidget(self.btn_salir)

        # Resultado
        self.resultado = QLabel("Resultado: ")
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def operar(self):
        try:
            n1 = float(self.num1.text())
            n2 = float(self.num2.text())

            if self.suma.isChecked():
                res = n1 + n2
            elif self.resta.isChecked():
                res = n1 - n2
            elif self.multi.isChecked():
                res = n1 * n2
            elif self.divi.isChecked():
                if n2 != 0:
                    res = n1 / n2
                else:
                    QMessageBox.warning(self, "Error", "No se puede dividir entre cero")
                    return
            else:
                QMessageBox.warning(self, "Error", "Seleccione una operación")
                return

            self.resultado.setText(f"Resultado: {res}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())