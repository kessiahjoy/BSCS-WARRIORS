from PIL import Image, ImageDraw, ImageFont


bg = Image.open("intrams.jpg")  # replace with your own file name
bg = bg.resize((1000, 700))  # resize to fit poster size


draw = ImageDraw.Draw(bg)


try:
    font_title = ImageFont.truetype("arial.ttf", 80)
    font_slogan = ImageFont.truetype("arial.ttf", 40)
except:
    font_title = ImageFont.load_default()
    font_slogan = ImageFont.load_default()

draw.text((200, 100), "BSCS WARRIORS", font=font_title, fill="blue")
draw.text((220, 220), "Unity in Spirit, Strength in Action", font=font_slogan, fill="red")


bg.save("PROFELEC2_4_PiocKessiahJoy_Activity1.png")
print("Poster created successfully with background!")
bg.show()
