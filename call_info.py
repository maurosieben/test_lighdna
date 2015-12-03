from PyQt4 import QtCore, QtGui
from info import Ui_Dialog
import sys

message = str(sys.argv[1])
#color = str(sys.argv[2])
class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #self.ui.msg.setStyleSheet('color : %s' %color)
        self.ui.msg.setText(message)
        self.ui.ok.clicked.connect(self.close)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())





