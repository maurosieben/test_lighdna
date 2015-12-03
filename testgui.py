#!/usr/bin/python
from PyQt4 import QtCore, QtGui, Qt
from testing import Ui_Dialog
import paho.mqtt.client as mqtt
from time import gmtime, strftime, sleep
import os
import sys
import subprocess
import atexit

ready = False
string = "Info: \n Espere as luminarias se conectarem e \n click em iniciar."
dev_list=list()
unity = "L000"
tag = 0
child_pid = 0
prog_dir = os.path.dirname(os.path.abspath(__file__))

def kill_child():
    global child_pid 
    csvF = open("%s/csv/registry.csv" %prog_dir,'w')
    csvF.close()
    if child_pid is None:
        pass
    else:
        child_pid+=1
        subprocess.call("kill -9 %d" %child_pid,shell=True)

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.create_list)
        self.ui.stop.clicked.connect(self.close)
        self.ui.fw.clicked.connect(self.next_tag)
        self.ui.bk.clicked.connect(self.prev_tag)
        self.ui.on.clicked.connect(self.ifon)
        self.ui.off.clicked.connect(self.ifoff)
        self.ui.ok.setStyleSheet("background-color: green; color: black")
        self.ui.nok.setStyleSheet("background-color: red; color: black")
        self.ui.play.clicked.connect(self.test_unity)
        self.ui.ok.clicked.connect(lambda:self.flip_status('ok'))
        self.ui.nok.clicked.connect(lambda:self.flip_status('off'))
        #self.ui.msg.setText("Clique em 'Iniciar' para come")
        global child_pid 
        prog = subprocess.Popen("python %s/register.py &" %prog_dir,shell=True ) 
        child_pid = prog.pid
        subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )

    # gets the tag out from error_log.csv file
    def takeout(self,dev):
        # checks it out if the file is empty, if it's writes default line
        f = open("%s/csv/error_log.csv" %prog_dir,'a+')
        if os.stat("%s/csv/error_log.csv" %prog_dir).st_size == 0:
            f.write('0000,XX-XX-XX-XX-XX-XX,L000,-1,-1,Grupo 1,Grupo 1.1,Grupo 1.1.1,0mA,100,1\n')
        f.close()
        f = open("%s/csv/error_log.csv" %prog_dir,'r')
        lines = f.readlines()
        f.close()
        f = open("%s/csv/error_log.csv" %prog_dir,'w')
        for line in lines:
            linecut = line.split(',')
            if linecut[0]!= dev_list[tag]:
                f.write(line)
        f.close()
    
    def addtested(self, line):
        # checks it out if the file is empty, if it's writes default line
        f = open("%s/csv/tested.csv" %prog_dir,'a+')
        if os.stat("%s/csv/tested.csv" %prog_dir).st_size == 0:
            f.write('0000,XX-XX-XX-XX-XX-XX,L000,-1,-1,Grupo 1,Grupo 1.1,Grupo 1.1.1,0mA,100,1\n')
        f.close()
        flag = False
        f = open("%s/csv/tested.csv" %prog_dir,'r')
        lines = f.readlines()
        f.close()
        ft = open("%s/csv/tested.csv" %prog_dir,'w')
        for linha in lines:
            linecut = linha.split(',')
            # see if there is a previous  related to the tag
            if linecut[0] == dev_list[tag]:
                flag = True
                ft.write(linha)
            else:
                ft.write(linha)
                # add the tag if it was not on the file before 
        if flag != True:
            ft.write(line)
        ft.close()
        
    def flip_status(self, status):
        # updates devive status on id.csv
        f=open("%s/csv/id.csv" %prog_dir,"r+")
        lines = f.readlines()
        f.close()
        #f=open("%s/csv/id.csv" %prog_dir,"w")
        for line in lines: 
            linecut = line.split(',')
            last =(len(linecut)-1)
            dev=linecut[0]
            if dev==dev_list[tag]:
                if status == 'ok':
                    self.takeout(dev)
                    '''if(linecut[last]=='1\n'):
                        f.write(line.replace('\n',',ok\n'))
                    elif(linecut[last]=='nok\n'):
                        f.write(line.replace('nok\n','ok\n'))
                    else:
                        f.write(line)
                    '''
                    self.addtested(line)
     
                else:
                    '''
                    if(linecut[last]=='1\n'):
                        f.write(line.replace('\n',',nok\n'))
                    elif(linecut[last]=='ok\n'):
                        f.write(line.replace('ok\n','nok\n'))
                    else:
                        f.write(line)
                    '''
                    subprocess.Popen("python %s/callog.py %s " %(prog_dir,unity),shell=True )
            '''else:
                f.write(line)
        f.close()
            '''
    def write_msg(self,string):
        self.ui.msg.setText(string)

    def prev_tag(self):
        if ready != True:
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )
            pass
        else:
            #increments tag variable and check it out if it is inside dev_list range
            global tag
            tag-=1
            if tag < 0: 
                tag=(len(dev_list)-1)
            self.start_test()
    
    def next_tag(self):
        if ready != True:
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )
            pass
        else:
            #increments tag variable ans check it out if it is inside dev_list range
            global tag
            tag+=1
            if tag > (len(dev_list)-1):
                tag=0
            self.start_test()
                
    def start_test(self):
        self.cancel = False 
        global unity,tag
        csvF= open("%s/csv/id.csv" %prog_dir,"r")
        for line in csvF:
            line = line.split(',')
            dev=line[0]
            if dev==dev_list[tag]:
                print dev
                print line[2]
                unity = line[2]
                self.ui.msg.setText("Luminaria %s sendo testada" %line[2])
                break
            else:
                self.ui.msg.setText("Luminaria com ID  %s nao consta no csv" %dev_list[tag])
        csvF.close()

    def create_list(self):
        global ready
        ready = True
        #create a list with all dev ID's on registry
        f= open("%s/csv/registry.csv" %prog_dir, "r+") 
        global dev_list
        del dev_list[:]
        for line in f:
            line=line.split(',')
            dev_list.append(line[0])
        f.close
#        for dev in dev_list:
#            print dev
        self.test_all()
        self.start_test()

    def test_all(self):
        # send command to all devices 
        client = mqtt.Client()
        client.connect("192.168.0.100", 1883, 60)
        client.publish("lights", "W0001-000")
        sleep(5)
        client.publish("lights", "W0001-018")
        sleep(5)
        client.publish("lights", "W0001-000")
        client.disconnect()
        
        
    def test_unity(self):
        if ready != True:
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )
            pass
        else:
            text = "Certifique-se que a tag '%s' confere \n na Luminaria" %unity
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,text),shell=True)
            # send command to the pointed device 
            dev_ID= dev_list[tag]
            client = mqtt.Client()
            client.connect("192.168.0.100", 1883, 60)
            client.publish("lights/%s" %dev_ID, "W0001-018")
            sleep(5)
            client.publish("lights/%s" %dev_ID, "W0001-000")
            client.disconnect()

    def ifon(self):
        if ready != True:
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )
            pass
        else:
            dev_ID= dev_list[tag]
            client = mqtt.Client()
            client.connect("192.168.0.100", 1883, 60)
            client.publish("lights/%s" %dev_ID, "W0001-100")
            client.disconnect()
    
    def ifoff(self):
        if ready != True:
            subprocess.Popen("python %s/call_info.py '%s'" %(prog_dir,string),shell=True )
            pass
        else:
            dev_ID= dev_list[tag]
            client = mqtt.Client()
            client.connect("192.168.0.100", 1883, 60)
            client.publish("lights/%s" %dev_ID, "W0001-000")
            client.disconnect()
        

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    atexit.register(kill_child)
    sys.exit(app.exec_())

