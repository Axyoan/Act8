from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from PySide2.QtGui import QIntValidator
from ui_mainwindow import Ui_MainWindow
from administrador_particulas import AdministradorParticula
from particula import Particula
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.administrador = AdministradorParticula()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.line_id.setValidator(QIntValidator(1, 1000))
        self.ui.line_velocity.setValidator(QIntValidator(1, 1000))
        self.ui.btnCreate_front.clicked.connect(self.click_create_front)
        self.ui.btnCreate_back.clicked.connect(self.click_create_back)
        self.ui.btn_show.clicked.connect(self.click_show)

    def clearInput(self):
        self.ui.line_id.setText("")
        self.ui.spinBox_xOrigin.setValue(0)
        self.ui.spinBox_yOrigin.setValue(0)
        self.ui.spinBox_xDestination.setValue(0)
        self.ui.spinBox_yDestination.setValue(0)
        self.ui.line_velocity.setText("")
        self.ui.spinBox_red.setValue(0)
        self.ui.spinBox_green.setValue(0)
        self.ui.spinBox_blue.setValue(0)

    def createParticle(self):
        p = Particula(int(self.ui.line_id.text()), self.ui.spinBox_xOrigin.value(), 
        self.ui.spinBox_yOrigin.value(), self.ui.spinBox_xDestination.value(), 
        self.ui.spinBox_yDestination.value(),int(self.ui.line_velocity.text()), 
        self.ui.spinBox_red.value(),self.ui.spinBox_green.value(),self.ui.spinBox_blue.value())
        return p

    @Slot()
    def click_create_front(self):
        if(self.ui.line_id.text()=="" or self.ui.line_velocity.text()==""):
            return; 
        self.administrador.agregar_inicio(self.createParticle())
        self.clearInput()

    @Slot()
    def click_create_back(self):
        if(self.ui.line_id.text()=="" or self.ui.line_velocity.text()==""):
            return; 
        self.administrador.agregar_final(self.createParticle())
        self.clearInput()

    @Slot()
    def click_show(self):
        self.ui.plainText.clear()
        self.ui.plainText.insertPlainText(str(self.administrador))