import sys
from random import randrange

import PyQt5
from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPainterPath, QPolygon
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('a.ui', self)
        self.pushButton.clicked.connect(self.pain)

    def pain(self):
        self.repaint()

    def paintEvent(self, event):
        len_storon = randrange(30, 400)
        qp = QPainter()
        qp.begin(self)
        self.paint(qp, len_storon)
        qp.end()

    def paint(self, qp, len_storon):
        qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
        x = randrange(0, 400 - len_storon)
        y = randrange(0, 400 - len_storon)
        qp.drawEllipse(x, y, len_storon, len_storon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a = Example()
    a.show()
    sys.exit(app.exec())