from PyQt5.QtWidgets import *
from PyQt5 import uic
from controller import *

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("mesin_kasir_GUI.ui", self)
        self.show()

        productsList = []
        self.btn_proses.clicked.connect(lambda: diproses(self,productsList))
        self.btn_hitung.clicked.connect(lambda: dihitung(self))
        self.btn_reset.clicked.connect(lambda: direset(self,productsList)) 

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()