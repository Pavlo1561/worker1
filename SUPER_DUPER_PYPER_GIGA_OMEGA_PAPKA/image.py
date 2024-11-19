from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

with Image.open("original.jpg") as pic_original:
    print("Розмір зображення: ", pic_original.size)
    print("Формат зображення: ", pic_original.format)
    print("Тип зображення: ", pic_original.mode)
    pic_original.show()

    pic_gray = pic_original.convert("L")
    pic_gray.save("gray.jpg")
    print("Розмір зображення: ", pic_gray.size)
    print("Формат зображення: ", pic_gray.format)
    print("Тип зображення: ", pic_gray.mode)
    pic_gray.show()

    pic_blured = pic_original.filter(ImageFilter.BLUR)
    pic_blured.save("blured.jpg")
    pic_blured.show()

    pic_up = pic_original.transpose(Image.ROTATE_180)
    pic_up.save("up.jpg")
    pic_up.show()

    pic_contrast = ImageEnhance.Contrast(pic_original)
    pic_contrast = pic_contrast.enhance (2)
    pic_contrast.save("contrast.jpg")
    pic_contrast.show()

    pic_mirrow = pic_original.transpose(Image.FLIP_LEFT_RIGHT)
    pic_mirrow.save("mirrow.jpg")
    pic_mirrow.show()