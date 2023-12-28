from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import *

app = QtWidgets.QApplication([])

#Uygulamanin ana penceresi

class Window(QtWidgets.QMainWindow):

    #constructor
    def __init__(self,title):

        super(Window,self).__init__()

        self.setWindowTitle(title)
        self.resize(600,500)

        self.login = QtWidgets.QWidget()
        self.login_config = Ui_login_widget()
        self.login_config.setupUi(self.login)

        self.menu = QtWidgets.QWidget()
        self.menu_config = Ui_menu_widget()
        self.menu_config.setupUi(self.menu)

        self.pages = QtWidgets.QStackedWidget()
        self.pages.addWidget(self.login)
        self.pages.addWidget(self.menu)
        self.pages.setCurrentWidget(self.login)

        self.setCentralWidget(self.pages)
        self.connect_buttons()

    def connect_buttons(self):

        self.login_config.boton.clicked.connect(self.log_in)
        self.menu_config.boton_salir.clicked.connect(lambda:self.change_page(self.login))

    def change_page(self,widget):
        
        self.pages.setCurrentWidget(widget)

    def log_in(self):

        username = self.login_config.textbox_usuario.text()

        if(len(username)>3):
            self.change_page(self.menu)
            self.menu_config.label_bienvenida.setText("Hoş geldiniz, "+username)


window = Window("ROTA Drawers")

window.show()
app.exec_()