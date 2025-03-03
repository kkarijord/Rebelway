import hou

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import*

class MyProject(QWidget):
    def __init__(self):
        super(MyProject,self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 318)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(110, 30, 171, 71))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(150, 170, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        #setup connections
        self.pushButton.clicked.connect(self.selectFile)
        

    def selectFile(self):
        directory= hou.ui.selectFile(file_type=hou.fileType.Directory)
        print(directory)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("Form", "PushButton", None, -1))

def show():
    houdini_window = hou.ui.mainQtWindow()
    this_widget = QtWidgets.QWidget(parent=houdini_window)

    window = MyProject()
    window.setupUi(this_widget)

    this_widget.setWindowTitle("Project Creator")
    this_widget.setWindowFlags(QtCore.Qt.Window)
    this_widget.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    this_widget.show()
    this_widget.ui = window
#show()


