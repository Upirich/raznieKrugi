from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt6.QtGui import QPainter, QPen, QColor, QPixmap
from random import randint
from PyQt6 import QtCore
import sys


class EllipsePainter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(600, 500)
        self.label = QLabel(self)
        self.label.resize(400, 400)
        self.pushButton = QPushButton(self)
        self.pushButton.resize(100, 60)
        self.pushButton.move(420, 420)
        self.pushButton.setText("kruzhochki")
        canvas = QPixmap(400, 400)
        canvas.fill(QtCore.Qt.GlobalColor.white)
        self.label.setPixmap(canvas)
        self.pushButton.clicked.connect(self.pon)

    def pon(self):
        canvas = self.label.pixmap()
        painter = QPainter(canvas)
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        painter.setPen(pen)
        n = randint(10, 200)
        n1 = randint(10, 300)
        n2 = randint(10, 300)
        painter.drawEllipse(n1, n2, n, n)
        self.label.setPixmap(canvas)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = EllipsePainter()
    ex.show()
    sys.exit(app.exec())
