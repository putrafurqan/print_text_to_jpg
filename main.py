from PIL import Image, ImageDraw, ImageFont, ImageOps
import textwrap


def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    #lines = textwrap.wrap(text, width=100)
    #for line in lines:
    img_fraction = 1
    fontsize = 1
    
    line_width, line_height = font.getsize(text)
    text_size = draw.textsize(text, font)
    image = image.resize(text_size)
    draw.text((30, 30), text, font=font, fill=text_color)



def main():
    '''
    Testing draw_multiple_line_text
    '''
    #image_width

    file_name = "input"
    image = Image.new('RGB', (1000, 1000), color = (255, 255, 255))
    fontsize = 12 # starting font size
    font = ImageFont.truetype("B:\\Programming\\cour.ttf", fontsize)
    file = open(file_name + ".txt","r")

    text1 = file.read()

    #add filename to the first line
    text1 = file_name + ".txt\n\n" + text1
    

    
    text_color = (0, 0, 0)
    text_start_height = 0
    font = ImageFont.truetype("B:\\Programming\\cour.ttf", fontsize)
    img_fraction = 0.1

    while font.getsize(text1)[0] < img_fraction*image.size[0]:
    # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype("B:\\Programming\\cour.ttf", fontsize)

    fontsize -= 1
    font = ImageFont.truetype("B:\\Programming\\cour.ttf", fontsize)
    draw_multiple_line_text(image, text1, font, text_color, text_start_height)
    image.save('output.png')

if __name__ == "__main__":
    main()