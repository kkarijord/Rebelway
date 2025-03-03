import hou

from PySide2 import QtCore, QtUiTools, QtWidgets, QtGui

class MyProject(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        scriptpath = hou.text.expandString("$RBW/UI_files/ui_ciro/project_creator.ui")
        self.ui = QtUiTools.QUiLoader().load(scriptpath, parentWidget=self)
        self.setParent(hou.qt.mainWindow(),QtCore.Qt.Window)
        self.setWindowTitle("Project Creator")
        self.setMaximumSize(400,400)

        ### SET CONNECTIONS
        self.sel_directory = self.ui.findChild(QtWidgets.QPushButton, "bt_directory")
        self.project_name = self.ui.findChild(QtWidgets.QLineEdit, "le_proj_name")
        self.project_code = self.ui.findChild(QtWidgets.QLineEdit, "le_proj")
        self.project_fps = self.ui.findChild(QtWidgets.QLineEdit, "le_fps")
        self.project_folders = self.ui.findChild(QtWidgets.QPlainTextEdit, "qpt_folders")
        self.create_project = self.ui.findChild(QtWidgets.QPushButton, "bt_create_project")

        ### SET VALUES

        self.project_name.setEnabled(False)
        self.project_code.setEnabled(False)
        self.project_fps.setEnabled(False)
        self.project_folders.setEnabled(False)
        self.create_project.setEnabled(False)
        

win = MyProject()
win.show()

#Ask for directory

#Check if is valid

# Request name, code, fps

#fps is an int

# Request or not default folders

# Create a project

#gather the info - dict

#check if the JSON exists - append

# if not create new file

#Window = with the information that was saved

#test

import hou
hou.ui.