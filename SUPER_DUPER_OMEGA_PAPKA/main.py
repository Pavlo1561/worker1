from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QInputDialog
from ui import Ui_MainWindow
import json

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.notes = {
                "Ласкаво просимо!" : {
                        "текст" : "Це найкращий додаток для заміток у світі!",
                        "теги" :["добро", "інструкція"]
                }
        }

        self.ui.list_notes.timeClicked.connect(self.show_note)

        self.load_notes()

    def add_note():
        note_name, ok = QInputDialog.getText(self.notes_win, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.notes[note_name] = {"текст": "", "теги" : []}
            self.ui.list_notes.addItem(note_name)
            self.ui.list_tags.addItems(self.note[note_name]["теги"])
            print(self.notes)
    def save_note():
        if list_notes.selectedItems()[0].text():
            notes[key]['текст'] = self.ui.note.toPlainText()
            with open('notes_data_json', 'w') as file:
                json.dump(notes,file,sort.keys==True, ensure_ascii=False)
            print(notes)
        else:
            print("Замітка для збереження не вибрана!")
        

    def del_note():
        if list_notes.selectedItems():

    def show_note(self):
        key = self.ui.list_notes.selectedItems()[0].text()
        self.ui.note.setText(self.notes[key]['текст'])
        self.ui.list_tags.clear()
        self.ui.list_tags.addItems(self.notes[key]["теги"])

    def load_notes(self):
        try:
            with open("notes_data.json", 'r') as file:
                self.notes = json.load(file)
            self.ui.list_notes.addItems(self.nottes)
        except:
            with open('notes_data.json', 'w') as file:
                json.dump(self.notes,file)
if __name__ == "__main__":
    app = QWidget.QApplication([])
    window = Widget()
    ex = Widget()
    ex.show()
    app.exec_()


#btn_note_crate
#btn_note_del
#btn_tag_add
#btn_tag_del
#btn_tag_search
#field_tag_2
#list_notes
#list_notes_label
#list_tags
#list_text_label
#note
#menubar
#statusbar
