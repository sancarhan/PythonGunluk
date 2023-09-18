import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from datetime import date

class GunlukUygulamasi(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Günlük Uygulaması")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.tarih_label = QLabel()
        self.tarih_label.setFont(QFont('Arial', 12))
        self.layout.addWidget(self.tarih_label)

        self.baslik_label = QLabel("Başlık:")
        self.layout.addWidget(self.baslik_label)

        self.baslik_input = QTextEdit()
        self.layout.addWidget(self.baslik_input)

        self.text_label = QLabel("Notlar:")
        self.layout.addWidget(self.text_label)

        self.text_input = QTextEdit()
        self.layout.addWidget(self.text_input)

        self.kaydet_button = QPushButton("Kaydet")
        self.kaydet_button.clicked.connect(self.kaydet)
        self.layout.addWidget(self.kaydet_button)

        self.central_widget.setLayout(self.layout)

        self.gunun_tarihi = date.today()
        self.tarih_label.setText(f"Tarih: {self.gunun_tarihi.strftime('%d/%m/%Y')}")

    def kaydet(self):
        tarih_str = self.gunun_tarihi.strftime('%Y-%m-%d')
        baslik = self.baslik_input.toPlainText()
        notlar = self.text_input.toPlainText()

        dosya_adi = f"{tarih_str}_{baslik}.docx"

        try:
            with open(dosya_adi, 'w') as dosya:
                dosya.write(notlar)
            print(f"{dosya_adi} başarıyla kaydedildi.")
        except Exception as e:
            print(f"Kaydetme hatası: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = GunlukUygulamasi()
    uygulama.show()
    sys.exit(app.exec_())
