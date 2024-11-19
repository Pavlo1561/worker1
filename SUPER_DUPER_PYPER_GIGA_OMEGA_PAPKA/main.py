from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

class ImageEditor():
    def __init__(self,filename):
        self.filename = filename
        self.original = None
        self.changed = []

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print("Файл не знайдено")
        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)
        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0]+str(len(self.changed))+".jpg"
        rotated.save(new_filename)

    def do_cropped(self):
        box = (250, 100, 600, 400)
        cropped = self.original.crop(box)
        self.changed.append(cropped)
        temp_filename = self.filename.split(".")
        new_filename = temp_filename[0]+str(len(self.changed))+".jpg"
        cropped.save(new_filename)




MyImage = ImageEditor("original.jpg")
MyImage.open()
MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()