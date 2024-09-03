from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QRadioButton,QMessageBox

def show_win():
    victory_win=QMessageBox()
    victory_win.setText('Ура! Ти виграв приватний літак !!!')
    victory_win.exec_()


def lol():
    lol_win=QMessageBox()
    lol_win.setText('Ти серйозно -_- ?')
    lol_win.exec_()


def lol2():
    lol2_win=QMessageBox()
    lol2_win.setText('💀')
    lol2_win.exec_()


def show_lose():
    victory_win=QMessageBox()
    victory_win.setText('Пощастить іншим разом!')
    victory_win.exec_()

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('CRAZY ПИТАННЯ')
my_win.move(100, 100)
my_win.resize(400, 400)

qestion = QLabel('Що таке PyQt5 ?')
btn_ans1=QRadioButton('Це профісійний інструмент, яким користуються багато програмістів')
btn_ans2=QRadioButton('Це Функція за допомогою якої можно додати значок')
btn_ans3=QRadioButton('Це те що заміняє нам print')
btn_ans4=QRadioButton('Я не знаю')
btn_ans5=QRadioButton('Це місто де можна зберігати усі модулі')
btn_ans6=QRadioButton('Усі відповіді вірні')

layout = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()


layoutH1.addWidget(qestion, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans4, alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_ans5, alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_ans6, alignment=Qt.AlignCenter)

layout.addLayout(layoutH1)
layout.addLayout(layoutH2)
layout.addLayout(layoutH3)
layout.addLayout(layoutH4)
my_win.setLayout(layout)

btn_ans3.clicked.connect(lol2)
btn_ans1.clicked.connect(show_win)
btn_ans2.clicked.connect(show_lose)
btn_ans4.clicked.connect(lol)
btn_ans5.clicked.connect(show_lose)
btn_ans6.clicked.connect(show_lose)


my_win.setStyleSheet("""
    QLabel {
        font-family: Arial, sans-serif;
        font-size: 20px;     
    }
    QWidget {
        background-color:#ADD8E6;
                            
    }
    QRadioButton{
        font-size: 14px;
        background-color: #00FFFF;
        color: black;
        padding: 10px;
        border-radius: 10px;                
                    
    }
    QRadioButton:hover {
        background-color: #00FFFF;        
    }
""")

my_win.show()
app.exec_()