import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


def window():
    app = QApplication(sys.argv)
    w = QWidget()
    # Crear un botón y adjuntarlo al widget w
    b = QPushButton(w)
    b.setText("Press me")
    b.move(50, 50)
    # Indicar al botón b que llame esta función cuando reciba un click
    # Nótese la falta de "()" en la llamada de la función
    b.clicked.connect(showdialog)
    w.setWindowTitle("PyQt Dialog")
    w.show()
    sys.exit(app.exec_())

# Esta función debería crear una ventana de diálogo con un botón
# que espera a recibir un click y luego sale del programa
def showdialog():
    d = QDialog()
    b1 = QPushButton("ok", d)
    b1.move(50, 50)
    d.setWindowTitle("Dialog")
    # Esta modalidad le indica al popup que bloquee al padre mientras activo
    d.setWindowModality(Qt.ApplicationModal)
    # Al recibir un click me gustaría que el proceso termine
    b1.clicked.connect(sys.exit)
    d.exec_()

if __name__ == '__main__':
    window()