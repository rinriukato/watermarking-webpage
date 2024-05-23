from PIL import Image, ImageFont, ImageDraw, ImageOps


def watermark(path):
    image_path = path
    watermark_text = "SAMPLE "
    font_size = 75

    image = Image.open(image_path)

    # Watermark text proportional to the image size
    final_text = ""
    for i in range(int(image.size[0] / font_size)):
        for j in range(int(image.size[0] / font_size)):
            final_text += watermark_text
        final_text += '\n'

    watermark_text = Image.new('L', (image.size[0], image.size[1]))
    img_draw = ImageDraw.Draw(watermark_text)
    font = ImageFont.truetype('arial.ttf', font_size)

    img_draw.multiline_text(
        xy=(0, 0),
        text=final_text,
        fill=155,
        font=font,
        spacing=50,
        align='center'
    )

    watermark_rotate = watermark_text.rotate(15, expand=1)
    image.paste(ImageOps.colorize(watermark_rotate, (0, 0, 0), (0, 0, 0, 128)), (-50, -50), watermark_rotate)

    image.show()
    image.save("static/watermark/test.png")

    return "static/watermark/test.png"
