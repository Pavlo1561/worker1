class Wijet():
    def __init__(self,text_tital,x,y):
        self.text_tital=text_tital
        self.x=x
        self.y=y
    def print_info(self):

        print('Напис', self.text_tital)
        print('Розташування', self.x, self.y)

class Button(Wijet):
    def __init__(self, text_tital, x, y, is_clicked_bool):
        super().__init__(text_tital, x, y)
        self.is_clicked_bool = is_clicked_bool
    def click(self):
        self.is_clicked = True
        print('Ви заєрестровані')

lottery_button=Button('Брати участь', 100,100, False)
lottery_button.print_info()
answer=input('Хочете зареєструватися? (так / ні):')
if answer == 'так':
    lottery_button.click()
else:
    print('А шкода')