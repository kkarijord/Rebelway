import hou
from PySide2 import QtCore, QtUiTools, QtWidgets

class MyGui(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
    
        script_path = "C:/Users/kristian.karijord/Documents/Rebelway_python/scripts/python/myFirstGUI/my_first_gui.ui"
        self.load_ui = QtUiTools.QUiLoader().load(script_path, parentWidget=self)
        self.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
        
        self.load_ui.mainButton.clicked.connect(self.createMessage)
    
    def createMessage(self):
        hou.ui.displayMessage('Sjekk her a! Knappen funker til og med!')
            
        
        
        
# window_gui = MyGui()
# window_gui.show()