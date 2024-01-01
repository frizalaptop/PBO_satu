from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import controller

def tambahElement(parent,productsList, id):
    container = parent.list_frame
    l = len(productsList)
    price = '{:,}'.format(productsList[l-1][2] * productsList[l-1][3])
    label = QLabel(f'{productsList[l-1][3]}x - {productsList[l-1][1]}  {price}')
    label.setFont(QFont('Bodoni MT', 14))
    label.setAlignment(Qt.AlignRight)
    btn_remove = QPushButton('Hapus')
    btn_remove.clicked.connect(lambda: hapusElement(parent, container,id, productsList))
    btn_remove.setFixedWidth(50)
    btn_remove.setStyleSheet("background-color:rgb(255, 76, 76); color:white;")
    frame = QFrame(container)
    frame.setObjectName(id)
    frame_layout = QHBoxLayout()
    frame.setLayout(frame_layout)
    frame.setFixedHeight(40)
    frame_layout.addWidget(btn_remove)
    frame_layout.addWidget(label)
    frame.setStyleSheet("background-color: white;")
    container.layout().addWidget(frame)    
    parent.inp_kode.setText('')
    parent.inp_kuantitas.setText('')

def hapusElement(parent, container,id, productsList):
    widget = container.findChild(QFrame, id)
    widget.deleteLater()
    for product in productsList:
        if product[0] == id:
            item = product
            productsList.remove(item)
        if productsList == []:
            parent.inp_cash.setText('')
            parent.inp_cash.setEnabled(False)
            parent.btn_hitung.setEnabled(False)
    controller.ditotal(parent,productsList)
    controller.dihitung(parent)