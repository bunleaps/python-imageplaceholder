from PIL import Image, ImageDraw, ImageFont, ImageOps
import sys

def IDCardGen( id, name, dob, joined, address ):
    card = Image.open("card.jpg")

    id_prof = Image.open("profiles/1.jpg")
    id_prof = id_prof.resize((172, 192))

    cover = Image.new("RGB", (180, 50), color="#fff")

    d = ImageDraw.Draw(card)
    font = ImageFont.truetype("fonts/Montserrat-Regular.ttf", 23)
    d.text((270, 90), id, font=font, fill=("#000"))
    d.text((245, 165), name, font=font, fill=("#000"))
    d.text((245, 225), dob, font=font, fill=("#000"))
    d.text((245, 285), joined, font=font, fill=("#000"))
    d.text((245, 345), address, font=font, fill=("#000"))

    card.paste(id_prof, (35, 145))
    card.paste(cover, (30, 330))
    card.show()

IDCardGen("1200", "John Doe", "24 February, 1995", "20 March, 2019", "Apartment Complex")