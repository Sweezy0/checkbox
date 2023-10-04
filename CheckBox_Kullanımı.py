import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
verdana_font=QFont("Verdana",15)
class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBox Kullanımı")
        self.setGeometry(400,100,600,400)
        self.arayuz()
    def arayuz(self):
        self.yazi=QLabel("Merhaba Python",self)
        self.yazi.setFont(verdana_font)
        self.yazi.move(200,50)
        self.yazi.resize(300,20)

        self.isim_kutusu=QLineEdit(self)
        self.isim_kutusu.move(200,100)
        self.isim_kutusu.setPlaceholderText("Lütfen isminizi girin:")

        self.soyisim_kutusu=QLineEdit(self)
        self.soyisim_kutusu.move(200,150)
        self.soyisim_kutusu.setPlaceholderText("Lütfen soyisminizi girin:")

        self.erkek=QCheckBox("Erkek",self)
        self.erkek.move(200,200)

        self.kadın=QCheckBox("Kadın",self)
        self.kadın.move(280,200)

        self.buton_kaydet=QPushButton("Kaydet",self)
        self.buton_kaydet.setFont(verdana_font)
        self.buton_kaydet.move(200,300)
        self.buton_kaydet.clicked.connect(self.fonksiyon_kaydet)

        self.show()
    def fonksiyon_kaydet(self):
        isim=self.isim_kutusu.text()
        soyisim=self.soyisim_kutusu.text()

        if (self.erkek.isChecked()):
            print(f"İsminiz: {isim}--- Soyisminiz: {soyisim}--- Cinsiyetiniz: Erkek")
        else:
            print(f"İsminiz: {isim}--- Soyisminiz: {soyisim}--- Cinsiyetiniz: Kadın")
    
uygulama=QApplication(sys.argv)
pencere=Pencere()
sys.exit(uygulama.exec_())