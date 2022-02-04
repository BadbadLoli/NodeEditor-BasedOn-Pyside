import os
import sys
from PySide2.QtWidgets import *
import inspect

from nodeeditor.utils import loadStylesheet
from nodeeditor.node_editor_window import NodeEditorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wnd = NodeEditorWindow()
    module_path = os.path.dirname(inspect.getfile(wnd.__class__))

    loadStylesheet(os.path.join(module_path, 'qss/nodestyle.qss'))

    print('module_path:', module_path)

    sys.exit(app.exec_())
