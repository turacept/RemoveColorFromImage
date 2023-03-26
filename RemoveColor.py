from PIL import Image

tolerance = 35


def LoadImg(imgname):
    img = Image.open(imgname)

    img = img.convert("RGBA")

    pixels = img.load()

    for x in range(img.width):
        for y in range(img.height):
            current_color = pixels[x, y]

            if current_color[0] > 255 - tolerance and current_color[1] > 255 - tolerance and current_color[
                2] > 255 - tolerance:
                pixels[x, y] = (255, 255, 255, 0)

    img.save("output_image.png")
