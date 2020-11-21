from PyQt5 import uic
from PyQt5.QtWidgets import QDialog
from sqlite import cur, con


class AddCoffee(QDialog):
    def __init__(self, id=None):
        super(AddCoffee, self).__init__()
        self.id = id
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUi()

    def initUi(self):
        self.btn_save.clicked.connect(self.save)

    def save(self):
        name = self.line_name.text()
        stepen = self.line_stepen.text()
        molot = 1 if self.radioButton.isChecked() else 0
        description = self.line_description.text()
        price = self.line_price.text()
        gramm = self.line_gramm.text()
        if not self.id:
            cur.execute('''INSERT INTO coffee VALUES(NULL, ?, ?, ?, ?, ?, ?)''',
                        (name, stepen, molot, description, price, gramm))
        else:
            cur.execute('''UPDATE coffee SET sort = ?, roasters = ?, ground = ?, description = ?, 
                            price = ?, gramm = ? WHERE id = ?''',
                        (name, stepen, molot, description, price, gramm, self.id))
        con.commit()
        self.close()
