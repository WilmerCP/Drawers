from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

app = QApplication([])

class Login(QWidget):

    def __init__(self,stacked_layout):
        super(Login,self).__init__()

        self.stacked_layout = stacked_layout
        layout = QVBoxLayout()
        layout.setContentsMargins(75, 35, 75, 90)
        layout.setAlignment(Qt.AlignCenter)  # Center the layout both horizontally and vertically

        logo_image = QPixmap("images/logo.png").scaledToWidth(200)
        logo = QLabel()
        logo.setPixmap(logo_image)
        logo.setAlignment(Qt.AlignCenter) 

        title = QLabel("Çekmece düzeltme uygulaması")
        title.setAlignment(Qt.AlignCenter)
        title = self.set_font_size(title,16)

        box_title = QLabel("Kullanıcı adınızı giriniz:")
        box_title = self.set_font_size(box_title,12)

        text_box = QLineEdit()
        text_box.setFixedSize(260, 35) 
        text_box = self.set_font_size(text_box,11)
        text_box.setStyleSheet("QLineEdit { padding: 2px; }")

        button = QPushButton("Girin")
        button.setFixedSize(110, 40)
        button = self.set_font_size(button,12)  

        layout.addWidget(logo)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(box_title)
        layout.addSpacing(10)
        layout.addWidget(self.align_center(text_box))
        layout.addSpacing(10)
        layout.addWidget(self.align_center(button))

        self.setLayout(layout)

    def align_center(self,widget):

        h_layout = QHBoxLayout()
        h_layout.setAlignment(Qt.AlignCenter)
        h_layout.setContentsMargins(0,0,0,0)
        h_layout.addWidget(widget)
        dummy_widget = QWidget()
        dummy_widget.setLayout(h_layout)

        return dummy_widget
    
    def set_font_size(self,widget,size):

        widget_font = widget.font()
        widget_font.setPointSize(size)
        widget.setFont(widget_font)
        return widget




#Uygulamanin ana penceresi

class Window(QMainWindow):

    #constructor
    def __init__(self,title):

        super(Window,self).__init__()

        self.setWindowTitle(title)
        self.setFixedSize(500,500)

        pages = QStackedLayout()
        pages.addWidget(Login(pages))

        central_widget = QWidget()
        central_widget.setLayout(pages)

        self.setCentralWidget(central_widget)


window = Window("ROTA Drawers")

window.show()
app.exec_()