from PIL import Image, ImageDraw, ImageFont
import math


bg = Image.open("intrams.jpg") 
bg = bg.resize((1000, 700))  

draw = ImageDraw.Draw(bg)


try:
    font_title = ImageFont.truetype("arial.ttf", 80)
    font_slogan = ImageFont.truetype("arial.ttf", 40)
except:
    font_title = ImageFont.load_default()
    font_slogan = ImageFont.load_default()


draw.text((200, 100), "BSCS WARRIORS", font=font_title, fill="blue")
draw.text((220, 220), "Unity in Spirit, Strength in Action", font=font_slogan, fill="red")


def draw_star(draw, cx, cy, r, fill_color):
    points = []
    for i in range(10):
        angle = math.radians(i * 36)  # 360/10 = 36
        radius = r if i % 2 == 0 else r / 2
        x = cx + radius * math.cos(angle - math.pi/2)
        y = cy + radius * math.sin(angle - math.pi/2)
        points.append((x, y))
    draw.polygon(points, fill=fill_color, outline="black")


draw_star(draw, 500, 350, 40, "yellow")
draw_star(draw, 430, 370, 30, "orange")
draw_star(draw, 570, 370, 30, "lightblue")


diamond_points = [(500, 420), (540, 460), (500, 500), (460, 460)]
draw.polygon(diamond_points, fill="purple", outline="black")


draw.ellipse((380, 320, 400, 340), fill="black")   
draw.line((390, 320, 390, 280), fill="black", width=4)  


draw.ellipse((600, 320, 620, 340), fill="blue")    
draw.line((610, 320, 610, 270), fill="blue", width=4)  
draw.line((610, 270, 640, 260), fill="blue", width=4)  


bg.save("PROFELEC2_4_PiocKessiahJoy_Activity1.png")
print("Poster created successfully with perfect stars, diamond, and music notes!")
bg.show()
