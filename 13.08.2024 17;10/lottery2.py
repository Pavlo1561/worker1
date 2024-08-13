from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QRadioButton,QMessageBox

def show_win():
    victory_win=QMessageBox()
    victory_win.setText('Ви виграли зустріч з творцями каналу')
    victory_win.exec_()


def show_lose():
    victory_win=QMessageBox()
    victory_win.setText('Пощастить іншим разом!')
    victory_win.exec_()

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Конкурс від Crazy People')
my_win.move(100, 100)
my_win.resize(400, 200)

qestion = QLabel('Як звали першого ютуб-блогера, який набрав 10.000.000 підписників?')
btn_ans1=QRadioButton('PewDiePie')
btn_ans2=QRadioButton('Рет і Лінк')
btn_ans3=QRadioButton('SlivkiShow')
btn_ans4=QRadioButton('TheBrianMaps')
btn_ans5=QRadioButton('Mister Max')
btn_ans6=QRadioButton('EeOneGuy')

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

btn_ans3.clicked.connect(show_lose)
btn_ans1.clicked.connect(show_win)
btn_ans2.clicked.connect(show_lose)
btn_ans4.clicked.connect(show_lose)
btn_ans5.clicked.connect(show_lose)
btn_ans6.clicked.connect(show_lose)

my_win.show()
app.exec_()