from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from PyQt5.QtWidgets import QMainWindow
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
                    "теги" : ["добро", "інструкція"],
            }
        }
        self.load_notes()

        self.ui.list_notes.itemClicked.connect(self.show_note)
        self.ui.btn_note_crate.clicked.connect(self.add_note)
        self.ui.btn_note_save.clicked.connect(self.save_note)
        self.ui.btn_note_del.clicked.connect(self.del_note)
        self.ui.btn_tag_add.clicked.connect(self.add_tag)
        self.ui.btn_tag_del.clicked.connect(self.del_tag)
        self.ui.btn_tag_search.clicked.connect(self.search_tag)
        


    def add_note(self):
        note_name, ok = QInputDialog.getText(self, "Додати замітку", "Назва замітки: ")
        if ok and note_name != "":
            self.notes[note_name] = {"текст": "", "теги" : []}
            self.ui.list_notes.addItem(note_name)
            self.ui.list_tags.addItems(self.notes[note_name]["теги"])
            print(self.notes)
    def save_note(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            self.notes[key]['текст'] = self.ui.note.toPlainText()
            with open('notes_data_json', 'w', encoding='utf-8') as file: # encoding='utf-8' - спосіб кодування
                json.dump(self.notes,file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:
            print("Замітка для збереження не вибрана!")
        

    def del_note():
        if list_notes.selectedItems():
            key = list_notes.selectedItems()[0].text()
            del notes[key]
            list_notes.clear()
            list_tags.clear()
            field_text.clear()
            list_notes.addItems(notes)
            with open('notes_data.json', 'w') as file:
                json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    def del_note(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            del self.notes[key]
            self.ui.list_notes.clear()
            self.ui.list_tags.clear()
            self.ui.note.clear()
            self.ui.list_notes.addItems(self.notes)
            with open("notes_data.json", "w",encoding='utf-8') as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:        
            print("Замітка для вилучення не обрана!")

    def show_note(self):
        key = self.ui.list_notes.selectedItems()[0].text()
        self.ui.note.setText(self.notes[key]['текст'])
        self.ui.list_tags.clear()
        self.ui.list_tags.addItems(self.notes[key]["теги"])

    def load_notes(self):
        try:
            with open("notes_data.json", 'r', encoding='utf-8') as file:
                self.notes = json.load(file)
            self.ui.list_notes.addItems(self.nottes)
        except:
            with open('notes_data.json', 'w', encoding='utf-8') as file:
                json.dump(self.notes,file)

    def add_tag(self):
        if self.ui.list_notes.selectedItems():
            key = self.ui.list_notes.selectedItems()[0].text()
            tag = self.ui.field_tag_2.text()
            if not tag in self.notes[key]["теги"]:
                self.notes[key]["теги"].append(tag)
                self.ui.list_tags.addItem(tag)
                self.ui.field_tag_2.clear()
            with open("notes_data.json","w", encoding='utf-8') as file:
                json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
            print(self.notes)
        else:
            print('Замітка для додавання тега не обрана')



    def del_tag(self):
        if self.ui.list_tags.selectedItems():
            if self.ui.list_notes.selectedItems():
                key=self.ui.list_notes.selectedItems()[0].text()
                tag=self.ui.list_tags.selectedItems()[0].text()
                self.notes[key]['теги'].remove(tag)
                self.ui.list_tags.clear()
                self.ui.list_tags.addItems(self.notes[key]['теги'])
                with open("notes_data.json","w", encoding='utf-8') as file:
                    json.dump(self.notes, file, sort_keys=True, ensure_ascii=False)
                print(self.notes)
            else:
                print('Замітка не обрана!')
        else:
            print('Тег для вилучення не обраний!')



    def search_tag(self):
        print(self.ui.btn_tag_search.text())
        tag = self.ui.field_tag_2.text()
        if self.ui.btn_tag_search.text() == 'Шукати замітку по тегу' and tag:
            print(tag)
            notes_filtered = {}
            for note in self.notes:
                if  tag in self.notes[note]['теги']:
                    notes_filtered[note] = self.notes[note]
            self.ui.btn_tag_search.setText("Скинути пошук")
            self.ui.list_notes.clear()
            self.ui.list_tags.clear()
            self.ui.list_notes.addItems(notes_filtered)
            print(self.ui.btn_tag_search.text())
        elif self.ui.btn_tag_search.text() == "Скинути пошук":
            self.ui.field_tag_2.clear()
            self.ui.list_notes.clear()
            self.ui.list_tags.clear()
            self.ui.list_notes.addItems(self.notes)
            self.ui.btn_tag_search.setText("Шукати замітки по тегу")
            print(self.ui.btn_tag_search.text())
        else:
            pass


if __name__ == "__main__":
    app = QApplication([])
    ex = Widget()
    ex.show()
    app.exec_()
