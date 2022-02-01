from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

class QDMCutLine(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.line_points = []
        self._pen = QPen(Qt.white)
        self._pen.setWidthF(2.0)
        self._pen.setDashPattern([3, 3])

        self.setZValue(2)

    def boundingRect(self) -> QRectF:
        return QRectF(0, 0, 1, 1)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.NoBrush)
        painter.setPen(self._pen)

        poly = QPolygonF(self.line_points)
        painter.drawPolyline(poly)