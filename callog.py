#!/usr/bin/python
from PyQt4 import QtCore, QtGui, Qt
from log import Ui_Dialog
import os
import sys

dev= str(sys.argv[1])
prog_dir = os.path.dirname(os.path.abspath(__file__))

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.submit.clicked.connect(self.savelog)
        self.ui.label.setText("Descreva o problema com %s" %dev)
        
    # gets the tag out from tested.csv file
    def takeout(self,unity):
        # checks it out if the file is empty, if it's writes default line
        f = open("%s/csv/tested.csv" %prog_dir,'a+')
        if os.stat("%s/csv/tested.csv" %prog_dir).st_size == 0:
            f.write('0000,XX-XX-XX-XX-XX-XX,L000,-1,-1,Grupo 1,Grupo 1.1,Grupo 1.1.1,0mA,100,1\n')
        f.close()
        f = open("%s/csv/tested.csv" %prog_dir,'r')
        lines = f.readlines()
        f.close()
        f = open("%s/csv/tested.csv" %prog_dir,'w')
        for line in lines:
            linecut = line.split(',')
            if linecut[2] != unity:
                f.write(line)
        f.close()


    def savelog(self):
        # gets the content on text box and saves in a variable
        text = self.ui.errorin.toPlainText()
        #print text
        flag = False
        f= open("%s/csv/id.csv" %prog_dir,"r")
        lines = f.readlines()
        f.close()
        for line in lines:
            linecut = line.split(',')
            if linecut[2] == dev:
                self.takeout(dev)
                # checks it out if the file is empty, if it's writes default line
                f = open("%s/csv/error_log.csv" %prog_dir,'a+')
                if os.stat("%s/csv/error_log.csv" %prog_dir).st_size == 0:
                    f.write('0000,XX-XX-XX-XX-XX-XX,L000,-1,-1,Grupo 1,Grupo 1.1,Grupo 1.1.1,0mA,100,1\n')
                f.close()
                
                f = open("%s/csv/error_log.csv" %prog_dir,'r')
                elines = f.readlines()
                f.close()
                f = open("%s/csv/error_log.csv" %prog_dir,'w')
                for eline in elines:
                    elinecut = eline.split(',')
                    # see if there is a previous error log related to the tag
                    if elinecut[2] == dev:
                        # replace for the new one
                        flag = True
                        f.write(line.replace('\n',",%s\n" %text ))
                    else:
                        f.write(eline)
                # add the tag if it was not on the file before 
                if flag != True:
                    f.write(line.replace('\n',",%s\n" %text ))
                f.close()
                self.close()

        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
#    atexit.register(kill_child)
    sys.exit(app.exec_())
