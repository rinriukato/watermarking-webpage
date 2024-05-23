from PIL import Image, ImageFont, ImageDraw, ImageOps

IMAGE_PATH = "image.jpg"
WATERMARK_TEXT = "SAMPLE "
FONT_SIZE = 75

image = Image.open(IMAGE_PATH)

# Watermark text proportional to the image size
final_text = ""
for i in range(int(image.size[0] / FONT_SIZE)):
    for j in range(int(image.size[0] / FONT_SIZE)):
        final_text += WATERMARK_TEXT
    final_text += '\n'

watermark_text = Image.new('L', (image.size[0], image.size[1]))
img_draw = ImageDraw.Draw(watermark_text)
font = ImageFont.truetype('arial.ttf', FONT_SIZE)

img_draw.multiline_text(
    xy=(0, 0),
    text=final_text,
    fill=155,
    font=font,
    spacing=50,
    align='center'
)
watermark = watermark_text.rotate(15, expand=1)
image.paste(ImageOps.colorize(watermark, (0, 0, 0), (0, 0, 0, 128)),(-50,-50), watermark)

image.show()
# image.save("test.png")
