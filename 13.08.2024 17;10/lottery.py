from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QRadioButton,QMessageBox

def show_win():
    victory_win=QMessageBox()
    victory_win.setText('Правильно!\n Ви виграли гіроскутер')
    victory_win.exec_()


def show_lose():
    victory_win=QMessageBox()
    victory_win.setText('Ні, в 2015 році.\n Ви виграли фірмовий плакат')
    victory_win.exec_()

app = QApplication([])

my_win = QWidget()
my_win.setWindowTitle('Конкурс від Crazy People')
my_win.move(100, 100)
my_win.resize(400, 200)

qestion = QLabel('В якому році канал отримав" золоту кнопку "від YouTube?')
btn_ans1=QRadioButton('2005')
btn_ans2=QRadioButton('2010')
btn_ans3=QRadioButton('2015')
btn_ans4=QRadioButton('2020')


layout = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(qestion, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_ans2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_ans4, alignment=Qt.AlignCenter)

layout.addLayout(layoutH1)
layout.addLayout(layoutH2)
layout.addLayout(layoutH3)
my_win.setLayout(layout)

btn_ans3.clicked.connect(show_win)

btn_ans1.clicked.connect(show_lose)
btn_ans2.clicked.connect(show_lose)
btn_ans4.clicked.connect(show_lose)

my_win.show()
app.exec_()

