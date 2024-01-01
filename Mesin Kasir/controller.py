from products import products
from manipulator import *

def diproses(parent,productsList):
    doubleProduct = False
    
    for item in productsList:
        if item[0] == parent.inp_kode.text():
            doubleProduct = True
            
    if parent.inp_kode.text() == '':
        dierror(parent, "Kode produk tidak boleh kosong!") 

    elif parent.inp_kuantitas.text() == '':
        dierror(parent, "Kuantitas tidak boleh kosong!")  
        
    elif int(parent.inp_kuantitas.text()) < 1:
        dierror(parent, "Kuantitas harus di atas 0") 

    elif doubleProduct == True:
        dierror(parent, "Produk sudah dalam list")       

    else:
        for product in products:
            if parent.inp_kode.text() == product[0]:
                product[3] = int(parent.inp_kuantitas.text())
                productsList.append(product)
                parent.inp_cash.setEnabled(True)
                parent.btn_hitung.setEnabled(True)
                tambahElement(parent,productsList, product[0])
                ditotal(parent,productsList)
                dihitung(parent)
                return 0
        dierror(parent, "Kode produk tidak ditemukan") 
           
def ditotal(parent,productsList):
    i = 0
    total = 0
    while i < len(productsList):
        total += productsList[i][2] * productsList[i][3]
        i+=1      
    parent.data_total.setText(str('{:,}'.format(total)))

def dihitung(parent):
    try:
        total = int(parent.data_total.text().replace(',', ''))
    except ValueError:
        total = 0
    
    try:
        cash = int(parent.inp_cash.text().replace(',', ''))
    except ValueError:
        cash = 0
    
    value = cash - total
    parent.data_kembali.setText(str('{:,}'.format(value)))

def dierror(parent, msg):
    message = QMessageBox(parent)
    message.setWindowTitle('Error!')
    message.setText(msg)
    message.setFont(QFont('Bodoni MT',14))
    message.setStyleSheet("background-color: #ff7c7e;")
    message.exec()

def direset(parent, productsList):
    parent.inp_cash.setText('')
    parent.inp_cash.setEnabled(False)
    parent.btn_hitung.setEnabled(False)
    parent.data_total.setText('0')
    parent.data_kembali.setText('0')
    container = parent.list_frame
    if productsList:
        for product in productsList:
            widget = container.findChild(QFrame, product[0])
            if widget is not None:
                widget.deleteLater()
    productsList.clear()