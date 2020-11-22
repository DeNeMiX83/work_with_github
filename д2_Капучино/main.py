import sys
from edit_form import AddCoffee
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidget, QTableWidgetItem, QPushButton

from д2_Капучино.data.sqlite import cur


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(100, 100, 650, 550)

        self.table = QTableWidget(self)
        self.table.resize(650, 500)
        self.update_table()
        self.table.itemClicked.connect(self.edit_coffee)

        self.btn_add = QPushButton('Добавить', self)
        self.btn_add.move(280, 510)
        self.btn_add.clicked.connect(self.add_coffee)

    def edit_coffee(self, event):
        row = event.row()
        id = self.table.item(row, 0).text()
        data = cur.execute('''SELECT * FROM coffee WHERE id = ?''', (id,)).fetchone()
        id, name, stepen, molot, description, price, gramm = data
        dialog = AddCoffee(id)
        dialog.line_name.setText(name)
        dialog.line_stepen.setText(stepen)
        dialog.radioButton.setChecked(bool(molot))
        dialog.line_description.setText(description)
        dialog.line_price.setText(str(price))
        dialog.line_gramm.setText(str(gramm))
        dialog.exec()
        self.update_table()

    def add_coffee(self):
        dialog = AddCoffee()
        dialog.exec()
        self.update_table()

    def update_table(self):
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
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec())
