import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit ,QVBoxLayout, QHBoxLayout,QRadioButton,QPushButton,QComboBox,QMessageBox

from convert import ConverterLogic

class CurrencyConverter(QWidget):
    def __init__(self):
        super().__init__()

        self.logic = ConverterLogic()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Value Convertor')
        self.resize(300, 200)

        currencies = ['USD', 'EUR', 'UAH', 'GBP']

        self.amount_Label = QLabel('Сума:')
        self.amount_input = QLineEdit()

        self.from_currency_Label = QLabel('З валюти:')
        self.from_currency_combo = QComboBox()
        self.from_currency_combo.addItems(currencies)

        self.to_currency_Label = QLabel('У валюту:')
        self.to_currency_combo = QComboBox()
        self.to_currency_combo.addItems(currencies)

        self.result_label = QLabel('Результат:')
        self.result_display = QLabel('0.00')

        self.convert_button = QPushButton('Конвертувати')
        self.convert_button.clicked.connect(self.convert_currency)

        layout = QVBoxLayout()

        layout.addLayout(self.creat_hbox_layout(self.amount_Label, self.amount_input))
        layout.addLayout(self.creat_hbox_layout(self.from_currency_Label, self.from_currency_combo))
        layout.addLayout(self.creat_hbox_layout(self.to_currency_Label, self.to_currency_combo))
        layout.addLayout(self.creat_hbox_layout(self.result_label, self.result_display))

        

        layout.addWidget(self.convert_button)

        self.setLayout(layout)
        self.apply_styles()
        self.show()

    def creat_hbox_layout(self,label,widget):
        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(widget)
        return hbox

    def convert_currency(self):
        try:
            amount = float(self.amount_input.text())
            from_currency = self.from_currency_combo.currentText()
            to_currency = self.to_currency_combo.currentText()

            converted_amount = self.logic.convert(amount, from_currency, to_currency)
            self.result_display.setText(f'{converted_amount: .2f}')

        except ValueError:
            self.show_error_massage('invalid input', 'Please enter a valid number')


    def show_error_massage(self,title,massage):
        error_dialog = QMessageBox()
        error_dialog.setIcon(QMessageBox.Warning)
        error_dialog.setWindowTitle(title)
        error_dialog.setText(massage)
        error_dialog.exec_()

    def apply_styles(self):
        self.setStyleSheet("""
            Qlabel {
                font-family: Arial, sans-serif;
                font-size: 16px;
                           
            }
            QLineEdit {
                font-size: 14px;
                                
            }
            QPushButton{
                font-size: 14px;
                background-color: #00FFFF;
                color: black;
                padding: 10px;
                border-radius: 10px                
                           
            }
            QPushButton:hover {
                background-color: #00FFFF;        
            }
""")


        
if __name__ == '__main__':
    app = QApplication([])
    ex = CurrencyConverter()
    sys.exit(app.exec())

