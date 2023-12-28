#File that host the code generated with PyQt designer. Provides classes that contains a method that
#sets the configuration and design of widgets including log in page, menu page...

from PyQt5 import QtCore, QtGui, QtWidgets

#Log-in widget User interface:

class Ui_login_widget(object):
    def setupUi(self, login_widget):
        login_widget.setObjectName("login_widget")
        login_widget.resize(566, 446)
        self.verticalLayout = QtWidgets.QVBoxLayout(login_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(login_widget)
        self.frame.setMaximumSize(QtCore.QSize(500, 170))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.logo = QtWidgets.QLabel(self.frame)
        self.logo.setMaximumSize(QtCore.QSize(200, 110))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("images/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.verticalLayout_2.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.titulo = QtWidgets.QLabel(self.frame)
        self.titulo.setMaximumSize(QtCore.QSize(300, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.verticalLayout_2.addWidget(self.titulo, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(login_widget)
        self.frame_2.setMaximumSize(QtCore.QSize(500, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.texto_input = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.texto_input.setFont(font)
        self.texto_input.setObjectName("texto_input")
        self.verticalLayout_3.addWidget(self.texto_input, 0, QtCore.Qt.AlignLeft)
        self.textbox_usuario = QtWidgets.QLineEdit(self.frame_2)
        self.textbox_usuario.setMinimumSize(QtCore.QSize(200, 32))
        self.textbox_usuario.setMaximumSize(QtCore.QSize(400, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textbox_usuario.setFont(font)
        self.textbox_usuario.setStyleSheet("QLineEdit{\n"
"\n"
"padding:3px;\n"
"\n"
"}")
        self.textbox_usuario.setObjectName("textbox_usuario")
        self.verticalLayout_3.addWidget(self.textbox_usuario, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(login_widget)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.boton = QtWidgets.QPushButton(self.frame_3)
        self.boton.setMinimumSize(QtCore.QSize(104, 32))
        self.boton.setMaximumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.boton.setFont(font)
        self.boton.setObjectName("boton")
        self.verticalLayout_4.addWidget(self.boton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(login_widget)
        QtCore.QMetaObject.connectSlotsByName(login_widget)

    def retranslateUi(self, login_widget):
        _translate = QtCore.QCoreApplication.translate
        login_widget.setWindowTitle(_translate("login_widget", "Form"))
        self.titulo.setText(_translate("login_widget", "Çekmece düzeltme uygulaması"))
        self.texto_input.setText(_translate("login_widget", "Kullanıcı adınızı giriniz:"))
        self.boton.setText(_translate("login_widget", "Giriş yap"))

#Menu widget user interface:

class Ui_menu_widget(object):
    def setupUi(self, menu_widget):
        menu_widget.setObjectName("menu_widget")
        menu_widget.resize(584, 416)
        self.verticalLayout = QtWidgets.QVBoxLayout(menu_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_bienvenida = QtWidgets.QLabel(menu_widget)
        self.label_bienvenida.setMinimumSize(QtCore.QSize(0, 40))
        self.label_bienvenida.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_bienvenida.setFont(font)
        self.label_bienvenida.setStyleSheet("QLabel{\n"
"\n"
"margin-bottom:18px;\n"
"margin-left:22px;\n"
"\n"
"}")
        self.label_bienvenida.setObjectName("label_bienvenida")
        self.verticalLayout.addWidget(self.label_bienvenida)
        self.frame_2 = QtWidgets.QFrame(menu_widget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_titulo = QtWidgets.QLabel(self.frame_2)
        self.label_titulo.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_titulo.setFont(font)
        self.label_titulo.setObjectName("label_titulo")
        self.verticalLayout_3.addWidget(self.label_titulo, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter)
        self.frame_3 = QtWidgets.QFrame(menu_widget)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 152))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.boton_drawers = QtWidgets.QPushButton(self.frame_3)
        self.boton_drawers.setMinimumSize(QtCore.QSize(210, 40))
        self.boton_drawers.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.boton_drawers.setFont(font)
        self.boton_drawers.setObjectName("boton_drawers")
        self.verticalLayout_4.addWidget(self.boton_drawers)
        self.boton_buscar = QtWidgets.QPushButton(self.frame_3)
        self.boton_buscar.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.boton_buscar.setFont(font)
        self.boton_buscar.setObjectName("boton_buscar")
        self.verticalLayout_4.addWidget(self.boton_buscar)
        self.boton_salir = QtWidgets.QPushButton(self.frame_3)
        self.boton_salir.setMinimumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.boton_salir.setFont(font)
        self.boton_salir.setObjectName("boton_salir")
        self.verticalLayout_4.addWidget(self.boton_salir)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(menu_widget)
        QtCore.QMetaObject.connectSlotsByName(menu_widget)

    def retranslateUi(self, menu_widget):
        _translate = QtCore.QCoreApplication.translate
        menu_widget.setWindowTitle(_translate("menu_widget", "Form"))
        self.label_bienvenida.setText(_translate("menu_widget", "Hoş Geldin, "))
        self.label_titulo.setText(_translate("menu_widget", "Çekmece düzeltme sistemi"))
        self.boton_drawers.setText(_translate("menu_widget", "Çekmece görüntule"))
        self.boton_buscar.setText(_translate("menu_widget", "Eşya arama"))
        self.boton_salir.setText(_translate("menu_widget", "Çıkış yap"))
