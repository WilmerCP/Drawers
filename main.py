from PyQt5 import QtCore, QtGui, QtWidgets
from widgets import *
from tables import *
from functools import partial

app = QtWidgets.QApplication([])

#Uygulamanin ana penceresi

class Window(QtWidgets.QMainWindow):

    #constructor
    def __init__(self,title):

        super(Window,self).__init__()

        self.setWindowTitle(title)
        self.resize(600,500)
        self.current_data = False

        self.login = QtWidgets.QWidget()
        self.login_config = Ui_login_widget()
        self.login_config.setupUi(self.login)

        self.menu = QtWidgets.QWidget()
        self.menu_config = Ui_menu_widget()
        self.menu_config.setupUi(self.menu)

        self.drawers = QtWidgets.QWidget()
        self.drawers_config = Ui_drawers_widget()
        self.drawers_config.setupUi(self.drawers)

        self.table_view = QtWidgets.QWidget()
        self.table_config = Ui_table_view()
        self.table_config.setupUi(self.table_view)

        self.pages = QtWidgets.QStackedWidget()
        self.pages.addWidget(self.login)
        self.pages.addWidget(self.menu)
        self.pages.addWidget(self.drawers)
        self.pages.addWidget(self.table_view)
        self.pages.setCurrentWidget(self.login)

        self.setCentralWidget(self.pages)
        self.show_drawers()
        self.connect_buttons()

    def connect_buttons(self):

        self.login_config.boton.clicked.connect(self.log_in)
        self.menu_config.boton_salir.clicked.connect(lambda:self.change_page(self.login))
        self.menu_config.boton_drawers.clicked.connect(lambda:self.change_page(self.drawers))
        self.drawers_config.back_to_menu.clicked.connect(lambda:self.change_page(self.menu))
        self.drawers_config.new_drawer.clicked.connect(self.create_drawer)
        self.table_config.button_back.clicked.connect(lambda:self.change_page(self.drawers))
        self.table_config.button_add.clicked.connect(lambda: self.resize_table("add"))
        self.table_config.button_delete.clicked.connect(lambda: self.resize_table("delete"))
        self.table_config.button_edit.clicked.connect(self.edit_table)

    def change_page(self,widget):
        
        self.pages.setCurrentWidget(widget)

    def log_in(self):

        username = self.login_config.textbox_usuario.text()

        if(len(username)>3):
            self.change_page(self.menu)
            self.menu_config.label_bienvenida.setText("Hoş geldiniz, "+username)

    def refresh_drawers(self):

        layout = self.drawers_config.formLayout_2

        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()
        
        self.show_drawers()

    def delete_drawer(self,num):

        def callback(err):
            if(err is not None):
                print(err)
        deleteFile(str(num)+".csv",callback)

        self.refresh_drawers()

    def show_drawers(self):

        drawers_list = listDrawers()

        for i,value in enumerate(drawers_list):

            num = int(value[:-4])

            button_delete = QtWidgets.QPushButton(self.drawers_config.scrollAreaWidget)
            button_delete.setMinimumSize(QtCore.QSize(45, 50))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(10)
            button_delete.setFont(font)
            button_delete.setText("")
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("images/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            button_delete.setIcon(icon)
            button_delete.setIconSize(QtCore.QSize(20, 20))
            button_delete.setObjectName("delete_"+str(num))
            self.drawers_config.formLayout_2.setWidget(i+1, QtWidgets.QFormLayout.LabelRole,button_delete)
            
            #Partial function allows us to have the function with the fixated index parameter
            partial_function = partial(self.delete_drawer,num=num)
            button_delete.clicked.connect(partial_function)
            
            drawer = QtWidgets.QPushButton(self.drawers_config.scrollAreaWidget)
            drawer.setMinimumSize(QtCore.QSize(0, 50))
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            drawer.setFont(font)
            drawer.setText("Çekmece "+str(num))
            drawer.setObjectName("drawer_"+str(num))
            self.drawers_config.formLayout_2.setWidget(i+1, QtWidgets.QFormLayout.FieldRole,drawer)

            partial_function_2 = partial(self.show_table,num=num)
            drawer.clicked.connect(partial_function_2)

    def create_drawer(self):

        file_list = listDrawers()
        clean_list = []
        my_number = 1
        exit = False

        for i,filename in enumerate(file_list):
            clean_list.append(int(filename[:-4]))

        while(exit is False and my_number<=len(clean_list)):
            if(my_number is not clean_list[my_number-1]):
                exit = True
            else:
                my_number +=1
        
        def callback(err):
            if(err is not None):
                print(err)
            else:
                self.refresh_drawers()

        emptyFile(str(my_number)+".csv",callback)

    def show_table(self,num):

        self.currentTable = num
        self.pages.setCurrentWidget(self.table_view)
        self.table_config.title.setText("Çekmece "+str(num))
        table = self.table_config.tableWidget
        table.setEnabled(False)

        def callback(err,data):
            if(err is not None):
                print(err)
            else:
                self.current_data = data
                table.setRowCount(len(data))
                for i,row in enumerate(data):
                
                    table.setItem(i,0,QtWidgets.QTableWidgetItem(row["isim"]))
                    table.setItem(i,1,QtWidgets.QTableWidgetItem(row["kategori"]))
                    table.setItem(i,2,QtWidgets.QTableWidgetItem(row["miktar"]))

        readFile(str(num)+".csv",callback)

    def edit_table(self,num):

        table = self.table_config.tableWidget

        switch = {
            0 : "isim",
            1: "kategori",
            2: "miktar"
            }
        
        if(not table.isEnabled()):
            table.setEnabled(True)

        else:
            table.setEnabled(False)
            content = []
            for i in range(table.rowCount()):
                content.append({})
                for j in range(table.columnCount()):
                    try:
                        text = table.item(i,j).text()
                    except:
                        text = " "
                    finally:
                        content[i][switch[j]] = text
                    
            def callback(err):
                if(err is not None):
                    print(err)
                else:
                    self.current_data = content

            if(self.current_data != content):
                newFile(str(self.currentTable)+".csv",content,callback)

    def resize_table(self,operation):

        table = self.table_config.tableWidget
        amount = table.rowCount()

        if(operation == "add" and table.isEnabled()):
            table.setRowCount(amount+1)

        if(operation == "delete" and table.isEnabled()):
            table.setRowCount(amount-1)




window = Window("ROTA Drawers")

window.show()
app.exec_()