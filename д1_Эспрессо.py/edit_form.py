from PyQt5 import uic
from PyQt5.QtWidgets import QDialog


class Example(QDialog):
    def __init__(self):
        super(Example, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui')
        self.initUi()

    def initUi(self):
        pass