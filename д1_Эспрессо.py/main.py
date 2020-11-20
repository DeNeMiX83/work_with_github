import sys
from sqlite3 import connect

from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 650, 500)
        self.table = QTableWidget(self)
        self.table.resize(650, 500)
        title = 'ID, название сорта, степень обжарки, молотый/в зернах, описание вкуса, цена, ' \
                'объем упаковки'.split(', ')
        self.table.setColumnCount(len(title))
        self.table.setHorizontalHeaderLabels(title)
        self.table.setRowCount(0)
        data = cur.execute('''SELECT * FROM coffee''').fetchall()
        for i, row in enumerate(data):
            self.table.setRowCount(self.table.rowCount() + 1)
            for j, item in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(item)))
        self.table.resizeColumnsToContents()


if __name__ == '__main__':
    con = connect('coffee.db')
    cur = con.cursor()
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())
