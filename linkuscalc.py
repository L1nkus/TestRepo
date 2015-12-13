import sys
from mathfunctions import toBinary, toTrinary
from PyQt4 import QtGui
from math import sqrt

class Example(QtGui.QWidget):
    def __init__(self):

        super(Example, self).__init__()
        self.initUI()
        self.wie=4
    def initUI(self):

        inw=QtGui.QLineEdit(self)
        inw.move(130,80)
        self.lbl=QtGui.QLabel(self)
        self.lbl.move(130,120)
        inw.textChanged[str].connect(self.onInput)
        combo = QtGui.QComboBox(self)
        combo.move(10, 80)
        combo.addItem("toBinary")
        combo.addItem("toTrinary")
        combo.addItem("fromBinary")
        combo.addItem("fromTrinary")
        combo.addItem("Square Root")
        combo.activated[str].connect(self.onTypeSwitch)
        self.setWindowTitle("LinkusCalculator")
        self.resize(300, 200)
        self.center()
        self.show()
    def onTypeSwitch(self, item):
        if item=='Square Root': self.wie=1
        elif item=='fromBinary': self.wie=2
        elif item=='fromTrinary': self.wie=3
        elif item=='toBinary': self.wie=4
        else: self.wie=5
    def onInput(self, text):
        try:
            if text=='': self.lbl.setText('')
            elif self.wie==4: self.lbl.setText(toBinary(text))
            elif self.wie==5: self.lbl.setText(toTrinary(text))
            elif self.wie==1: self.lbl.setText(str(sqrt(float(text))))
            else: self.lbl.setText(str(int(text, self.wie)))
        except ValueError:
            self.lbl.setText("Value Error!")
        self.lbl.adjustSize()
    def center(self):

        qr=self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def main():
    app=QtGui.QApplication(sys.argv)
    GUI=Example()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()