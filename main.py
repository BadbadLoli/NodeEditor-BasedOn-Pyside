import sys
from PySide2.QtWidgets import *

if __name__ == '__main__':
    app = QApplication(sys.argv)

    label = QLabel("Hello, PyQt5!")
    label.show()

    sys.exit(app.exec_())
