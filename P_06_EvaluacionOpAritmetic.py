
import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "Prog_06_EvaluacionOpAritmetic.ui"
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)

class Myapp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.Bcalcular.clicked.connect(self.calcular)

    def calcular(self):
        exprecion = self.Lexp.text()
        result = eval(exprecion)
        print(result)
        self.Lresultado.setText(str(result))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Myapp()
    window.show()
    sys.exit(app.exec_())