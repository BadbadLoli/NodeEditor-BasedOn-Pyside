from PySide2.QtWidgets import *

class CalculatorWindow(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.initUI()

    def initUI(self):
        pass
