from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem, QGraphicsScene
from PySide2.QtGui import QPen, QColor, QTransform
from PySide2.QtCore import Slot
from PySide2.QtGui import QIntValidator
from random import randint
from ui_mainwindow import Ui_MainWindow
from administrador_particulas import AdministradorParticula
from particula import Particula
from pprint import pformat, pprint


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.administrador = AdministradorParticula()
        self.graph = dict()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.line_id.setValidator(QIntValidator(1, 1000))
        self.ui.line_velocity.setValidator(QIntValidator(1, 1000))
        self.ui.btnCreate_front.clicked.connect(self.click_create_front)
        self.ui.btnCreate_back.clicked.connect(self.click_create_back)
        self.ui.btn_show.clicked.connect(self.click_show)
        self.ui.actionAbrir.triggered.connect(self.action_open_file)
        self.ui.actionGuardar.triggered.connect(self.action_save_file)
        self.ui.actionGrafo.triggered.connect(self.showGraph)
        self.ui.pushButton_read.clicked.connect(self.readTable)
        self.ui.pushButton_showTable.clicked.connect(self.showTable)
        self.ui.pushButton_draw.clicked.connect(self.draw)
        self.ui.pushButton_clear.clicked.connect(self.clearScreen)
        self.ui.pushButton_sortId.clicked.connect(self.sortIdAsc)
        self.ui.pushButton_sortDistance.clicked.connect(self.sortDistanceDesc)
        self.ui.pushButton_sortVelocity.clicked.connect(self.sortVelocityAsc)

        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

    def insertVertex(self, p):
        if (p.origen_x, p.origen_y) in self.graph:
            self.graph[(p.origen_x, p.origen_y)].append(
                ((p.destino_x, p.destino_y), p.distancia))
        else:
            self.graph[(p.origen_x, p.origen_y)] = [
                ((p.destino_x, p.destino_y), p.distancia)]

        if((p.destino_x, p.destino_y)) in self.graph:
            self.graph[(p.destino_x, p.destino_y)].append(
                ((p.origen_x, p.origen_y), p.distancia))
        else:
            self.graph[(p.destino_x, p.destino_y)] = [
                ((p.origen_x, p.origen_y), p.distancia)]

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
                      self.ui.spinBox_yDestination.value(), int(self.ui.line_velocity.text()),
                      self.ui.spinBox_red.value(), self.ui.spinBox_green.value(), self.ui.spinBox_blue.value())
        return p

    def setTableHeaders(self):
        self.ui.tableWidget.setColumnCount(10)
        headers = ["id", "Origen x", "Origen y", "Destino x",
                   "Destino y", "Velocidad", "Red", "Green", "Blue", "Distancia"]
        self.ui.tableWidget.setHorizontalHeaderLabels(headers)

    def createRow(self, particula, rowCount):
        self.setTableHeaders()
        id_widget = QTableWidgetItem(str(particula.id))
        origen_x_widget = QTableWidgetItem(str(particula.origen_x))
        origen_y_widget = QTableWidgetItem(str(particula.origen_y))
        destino_x_widget = QTableWidgetItem(str(particula.destino_x))
        destino_y_widget = QTableWidgetItem(str(particula.destino_y))
        velocidad_widget = QTableWidgetItem(str(particula.velocidad))
        red_widget = QTableWidgetItem(str(particula.red))
        blue_widget = QTableWidgetItem(str(particula.blue))
        green_widget = QTableWidgetItem(str(particula.green))
        distancia_widget = QTableWidgetItem(str(particula.distancia))
        self.ui.tableWidget.setItem(rowCount, 0, id_widget)
        self.ui.tableWidget.setItem(rowCount, 1, origen_x_widget)
        self.ui.tableWidget.setItem(rowCount, 2, origen_y_widget)
        self.ui.tableWidget.setItem(rowCount, 3, destino_x_widget)
        self.ui.tableWidget.setItem(rowCount, 4, destino_y_widget)
        self.ui.tableWidget.setItem(rowCount, 5, velocidad_widget)
        self.ui.tableWidget.setItem(rowCount, 6, red_widget)
        self.ui.tableWidget.setItem(rowCount, 7, green_widget)
        self.ui.tableWidget.setItem(rowCount, 8, blue_widget)
        self.ui.tableWidget.setItem(rowCount, 9, distancia_widget)

    def wheelEvent(self, event):
        if event.delta() > 0:
            self.ui.graphicsView.scale(1.2, 1.2)
        else:
            self.ui.graphicsView.scale(0.8, 0.8)

    @Slot()
    def readTable(self):
        self.setTableHeaders()
        idFound = self.ui.lineEdit_read.text()
        for particula in self.administrador:
            if idFound == str(particula.id):
                self.ui.tableWidget.clear()
                self.ui.tableWidget.setRowCount(1)
                self.createRow(particula, 0)
                return
        QMessageBox.warning(
            self, "Atención", f'La partícula con id "{id}" no se encontró')

    @Slot()
    def showTable(self):
        self.ui.tableWidget.setRowCount(len(self.administrador))
        row_count = 0
        for particula in self.administrador:
            self.createRow(particula, row_count)
            row_count += 1

    @ Slot()
    def action_open_file(self):
        directory = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.open_file(directory):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo abrir el archivo "+directory
            )
            for p in self.administrador:
                self.insertVertex(p)
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo abrir el archivo "+directory
            )

    @Slot()
    def action_save_file(self):
        directory = QFileDialog.getSaveFileName(
            self,
            'Guardar Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.save_file(directory):
            QMessageBox.information(
                self,
                "Éxito",
                "Se pudo guardar el archivo "+directory
            )
        else:
            QMessageBox.critical(
                self,
                "Error",
                "No se pudo guardar el archivo "+directory
            )

    @Slot()
    def click_create_front(self):
        if(self.ui.line_id.text() == "" or self.ui.line_velocity.text() == ""):
            return
        p = self.createParticle()
        self.administrador.agregar_inicio(p)
        self.insertVertex(p)
        self.clearInput()

    @Slot()
    def click_create_back(self):
        if(self.ui.line_id.text() == "" or self.ui.line_velocity.text() == ""):
            return
        p = self.createParticle()
        self.administrador.agregar_final(p)
        self.insertVertex(p)
        self.clearInput()

    @Slot()
    def click_show(self):
        self.ui.plainText.clear()
        self.ui.plainText.insertPlainText(str(self.administrador))

    @Slot()
    def draw(self):
        pen = QPen()
        pen.setWidth(2)
        for particula in self.administrador:
            color = QColor(particula.red, particula.green, particula.blue)
            pen.setColor(color)
            xs = particula.origen_x
            xf = particula.destino_x
            ys = particula.origen_y
            yf = particula.destino_y
            self.scene.addEllipse(xs, ys, 3, 3, pen)
            self.scene.addEllipse(xf, yf, 3, 3, pen)
            self.scene.addLine(xs, ys, xf, yf, pen)

    @Slot()
    def clearScreen(self):
        self.scene.clear()

    @Slot()
    def sortIdAsc(self):
        self.administrador.sort(lambda particula: particula.id, False)
        self.click_show()
        self.showTable()

    @Slot()
    def sortDistanceDesc(self):
        self.administrador.sort(lambda particula: particula.distancia, True)
        self.click_show()
        self.showTable()

    @Slot()
    def sortVelocityAsc(self):
        self.administrador.sort(lambda particula: particula.velocidad, False)
        self.click_show()
        self.showTable()

    @Slot()
    def showGraph(self):
        str_g = pformat(self.graph, width=40, indent=1)
        print(str_g)
        self.ui.plainText.clear()
        self.ui.plainText.insertPlainText(str_g)
