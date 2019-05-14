# References:
# https://stackoverflow.com/questions/44370469/python-image-resizing-keep-proportion-add-white-background
# https://github.com/python-pillow/Pillow/issues/2609

from PIL import Image

def squareImage(image):

    try:
        image_size = image.size
        width = image_size[0]
        height = image_size[1]

        fill_color = ''  # your background
        if image.mode in ('RGBA', 'LA'):
            background = Image.new(image.mode[:-1], image.size, (255, 255, 255, 255))
            background.paste(image, image.split()[-1])
            image = background

        if(width != height):
            bigside = width if width > height else height

            background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
            offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

            background.paste(image, offset)
            image = background
            print("Image has been squared!")

        else:
            print("Image is already a square, it has not been resized !")

        image = image.convert("RGB")
        return image
    except:
        print("[INFO] error processing image")