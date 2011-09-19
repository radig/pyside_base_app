import os, sys

from db import config
from elixir import *
from PySide import QtCore, QtGui
from views import ui_window, ui_dialog

from models import user

class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.ui = ui_dialog.Ui_Dialog()
        self.ui.setupUi(self)

class Main(QtGui.QMainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.ui = ui_window.Ui_MainWindow()
        self.ui.setupUi(self)
        
        QtCore.QObject.connect(self.ui.actionOpenFile,QtCore.SIGNAL("triggered()"), self.change_tab)
        QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.open_window)
        
        for u in user.User.query.all():
            item = QtGui.QTreeWidgetItem([u.name, u.lastname, u.phone])
            self.ui.userList.addTopLevelItem(item)
    
    def change_tab(self):
        currentIndex = self.ui.tabWidget.indexOf(self.ui.userListTab)
        self.ui.tabWidget.setCurrentIndex(currentIndex)
    
    def open_window(self):
        window2 = Dialog()
        window2.exec_()
    
    def file_dialog(self):
        fd = QtGui.QFileDialog(self)
        self.filename = fd.getOpenFileName()
        from os.path import isfile
        if isfile(self.filename):
            text = open(self.filename).read()
            self.ui.textEdit.setText(text)

def main():
    config.initDB()
    
    # fulano=user.User(name="Fulano", lastname="Souza", phone="123")
    # joao=user.User(name="Joao", lastname="da Silva", phone="321")
    # session.commit()
    
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()