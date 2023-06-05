from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QDialog,
    QLineEdit,
)
from PyQt5 import QtCore


class Swiatla(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(180, 500)
        self.layout = QVBoxLayout()
        self.czerwone = QPushButton("")
        self.zolte = QPushButton("")
        self.zielone = QPushButton("")
        self.layout.addWidget(self.czerwone)
        self.layout.addWidget(self.zolte)
        self.layout.addWidget(self.zielone)
        self.layout.setSpacing(10)
        self.setStyleSheet(
            "QPushButton { border: 1px solid black; border-radius: 75px; padding: 0px; margin: 0px} QWidget {background-color: black;} "
        )
        self.czerwone.setFixedSize(150, 150)
        self.zielone.setFixedSize(150, 150)
        self.zolte.setFixedSize(150, 150)
        self.setLayout(self.layout)
        self.show()
        self.timer = QtCore.QTimer()
        self.zielonyf()

    def zielonyf(self):
        self.zielone.setStyleSheet("background-color:green")
        self.zolte.setStyleSheet("background-color:black")
        self.czerwone.setStyleSheet("background-color:black")
        self.timer.singleShot(5000, lambda: self.zoltyf(0))

    def zoltyf(self, ktory):
        self.zielone.setStyleSheet("background-color:black")
        self.zolte.setStyleSheet("background-color:yellow")
        self.czerwone.setStyleSheet("background-color:black")
        if ktory == 0:  # czerwony
            self.timer.singleShot(2000, self.czerwonyf)
        if ktory == 1:  # zielony
            self.timer.singleShot(2000, self.zielonyf)

    def czerwonyf(self):
        self.zielone.setStyleSheet("background-color:black")
        self.zolte.setStyleSheet("background-color:black")
        self.czerwone.setStyleSheet("background-color:red")
        self.timer.singleShot(5000, lambda: self.zoltyf(1))


app = QApplication([])
nowe = Swiatla()
app.exec_()
