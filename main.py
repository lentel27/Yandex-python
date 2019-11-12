import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPen, QPainter
from PyQt5.QtCore import Qt
from PyQt5 import uic
import random


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.draw = False
        self.circle_add.clicked.connect(self.trueDraw)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawFlag(qp)
        self.update()
        qp.end()

    def drawFlag(self, qp):
        qp.setPen(Qt.black)
        qp.setBrush(Qt.black)
        qp.drawRect(0, 0, self.width(), self.height())
        if self.draw:
            qp.setPen(Qt.yellow)
            size = random.randrange(100, 500)
            qp.drawEllipse(random.randrange(-100, self.width()),
                           random.randrange(-100, self.height()),
                           size, size)

    def trueDraw(self):
        self.draw = True


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())