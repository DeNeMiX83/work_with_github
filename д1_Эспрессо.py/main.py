import sys

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 500, 500)
        self.table = QTableWidget(self)
        self.table.resize(500, 500)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())
