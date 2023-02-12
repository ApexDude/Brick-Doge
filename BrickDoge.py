import random

WIDTH = 1000
HEIGHT = 500

player = Actor("player.png")
player.pos = 200, 250

background = Actor("background.jpg")
tint = Actor("tint.png")
ptint = Actor("tint.png")
tot = Actor("help")

#buttons
play = Actor("play")
play.pos = 500, 250
bhelp = Actor("levels")
bhelp.pos = 500, 400
back = Actor("back")
back.pos = 25, 25

flap = 1
game = 1
m = game

pscore = 0

point5 = Actor("5point.png")
point5.pos = random.randint(2000, 4000), random.randint(125, 375)

score = 0

vew = 0.5
speed = 2
gravity = 2


p1 = Actor("p1.png")
p1.pos = 500, random.randint(-100, 100)

p2 = Actor("p1.png")
p2.pos = 800, random.randint(-100, 100)

p3 = Actor("p1.png")
p3.pos = 1100, random.randint(-100, 100)

p4 = Actor("p1.png")
p4.pos = 1400, random.randint(-100, 100)

setscore = 0

p5 = Actor("p1.png")
p5.pos = 1700, random.randint(-100, 100)

p_1 = Actor("p1.png")
p_1.pos = p1.x, (p1.y+600)

p_2 = Actor("p1.png")
p_2.pos = p2.x, (p2.y+600)

p_3 = Actor("p1.png")
p_3.pos = p3.x, (p3.y+600)

p_4 = Actor("p1.png")
p_4.pos = p4.x, (p4.y+600)

p_5 = Actor("p1.png")
p_5.pos = p5.x, (p5.y+600)

def update(pos):
    global speed, game, flap, score, pscore, setscore
    #Score system
    if player.x == p1.x:
        score += 1
    if player.x == p2.x:
        score += 1
    if player.x == p3.x:
        score += 1
    if player.x == p4.x:
        score += 1
    if player.x == p5.x:
        score += 1
    #bonus point
    if player.colliderect(point5):
        score += 1
    if point5.colliderect(p1) or point5.colliderect(p2) or point5.colliderect(p3) or point5.colliderect(p4) or point5.colliderect(p5) or point5.colliderect(p_1) or point5.colliderect(p_2) or point5.colliderect(p_3) or point5.colliderect(p_4) or point5.colliderect(p_5):
        point5.y -= 5
    #death system
    if player.colliderect(p1) or player.colliderect(p2) or player.colliderect(p3) or player.colliderect(p4) or player.colliderect(p5) or player.colliderect(p_1) or player.colliderect(p_2) or player.colliderect(p_3) or player.colliderect(p_4) or player.colliderect(p_5):
        screen.draw.text("oops you lost, click to play again!", (350,250), fontname="pencil", fontsize=50)
        screen.draw.text(f"you score is {str(pscore)}", (500,300), fontname="pencil", fontsize=50)
        p1.pos = 500, random.randint(-100, 100)
        p2.pos = 800, random.randint(-100, 100)
        p3.pos = 1100, random.randint(-100, 100)
        p4.pos = 1400, random.randint(-100, 100)
        p5.pos = 1700, random.randint(-100, 100)
        p_1.pos = p1.x, (p1.y+600)
        p_2.pos = p2.x, (p2.y+600)
        p_3.pos = p3.x, (p3.y+600)
        p_4.pos = p4.x, (p4.y+600)
        p_5.pos = p5.x, (p5.y+600)
        player.pos = 200, 250
        game = 2
        score = 0
    #home page
    if game == 1:
        screen.clear()
        background.draw()
        screen.draw.text(f"Brick Doge", (320,100), fontname="pencil", fontsize=100, color="black")
        play.draw()
        bhelp.draw()
        screen.draw.text("Made By Advaith Rajesh", (775, 475), fontname="pencil", fontsize=25, color="black")
    if game == 4:
        screen.clear()
        background.draw()
        screen.draw.text(f"Brick Doge", (320,100), fontname="pencil", fontsize=100, color="black")
        screen.draw.text("Made By Advaith Rajesh", (775, 475), fontname="pencil", fontsize=25, color="black")
        tot.draw()
        back.draw()
    #main game
    if game == 2:
        player.pos = 200, 250
        point5.pos = random.randint(2000, 4000), random.randint(125, 375)
        screen.clear()
        background.draw()
        score = 0
        p1.draw()
        p2.draw()
        p3.draw()
        p4.draw()
        p5.draw()
        p_1.draw()
        p_2.draw()
        p_3.draw()
        p_4.draw()
        p_5.draw()
        point5.draw()
        player.draw()
        tint.draw()
        background.pos = 500, 500
        screen.draw.text("Click To Start", (250,150), fontname="cartoonblocks", fontsize=50)
        screen.draw.text(f"Your high score: {str(pscore)}", (300,220), fontname="pencil", fontsize=50)
        screen.draw.text(f"Your score: {str(setscore)}", (350, 270), fontname="pencil", fontsize=50)
        screen.draw.text("Made By Advaith Rajesh", (775, 475), fontname="pencil", fontsize=25, color="grey")
    if game == 3:
        screen.clear()
        background.draw()
        setscore = score
        p1.draw()
        p2.draw()
        p3.draw()
        p4.draw()
        p5.draw()
        p_1.draw()
        p_2.draw()
        p_3.draw()
        p_4.draw()
        p_5.draw()
        point5.draw()
        player.draw()
        point5.right -= speed
        screen.draw.text(f"{str(score)}", (500, 100), fontname="starwars", color="orange", fontsize=50)
        background.left -= vew
        if score > pscore:
            pscore = score
        if background.left < -1000:
            background.x = 500
        p_1.right -= speed
        if p_1.right < 0:
            p_1.right = 1500
            p_1.pos = p1.x, (p1.y+600)
        p_2.right -= speed
        if p_2.right < 0:
            p_2.right = 1500
            p_2.pos = p2.x, (p2.y+600)
        p_3.right -= speed
        if p_3.right < 0:
            p_3.right = 1500
            p_3.pos = p3.x, (p3.y+600)
        p_4.right -= speed
        if p_4.right < 0:
            p_4.right = 1500
            p_4.pos = p4.x, (p4.y+600)
        p_5.right -= speed
        if p_5.right < 0:
            p_5.right = 1500
            p_5.pos = p5.x, (p5.y+600)
        if speed < 0:
            speed = 0
        p1.right -= speed
        if p1.right < 0:
            p1.right = 1500
            p1.pos = 1500, random.randint(-100, 100)
        p2.right -= speed
        if p2.right < 0:
            p2.right = 1500
            p2.pos = 1500, random.randint(-100, 100)
        p3.right -= speed
        if p3.right < 0:
            p3.right = 1500
            p3.pos = 1500, random.randint(-100, 100)
        p4.right -= speed
        if p4.right < 0:
            p4.right = 1500
            p4.pos = 1500, random.randint(-100, 100)
        p5.right -= speed
        if p5.right < 0:
            p5.right = 1500
            p5.pos = 1500, random.randint(-100, 100)
        if player.y > 500:
            game = 2
            player.pos = 200, 250
            screen.draw.text("oops you lost, click to play again!", (350,250), fontname="pencil", fontsize=50)
            screen.draw.text(f"you score is {str(pscore)}", (500,300), fontname="pencil", fontsize=50)
            p1.pos = 500, random.randint(-100, 100)
            p2.pos = 800, random.randint(-100, 100)
            p3.pos = 1100, random.randint(-100, 100)
            p4.pos = 1400, random.randint(-100, 100)
            p5.pos = 1700, random.randint(-100, 100)
            p_1.pos = p1.x, (p1.y+600)
            p_2.pos = p2.x, (p2.y+600)
            p_3.pos = p3.x, (p3.y+600)
            p_4.pos = p4.x, (p4.y+600)
            p_5.pos = p5.x, (p5.y+600)
        if flap == 1:
            player.y += gravity
        if flap == 2:
            player.y -= gravity
        screen.draw.text("Made By Advaith Rajesh", (775, 475), fontname="pencil", fontsize=25, color="black")

#controls
def on_mouse_down(pos, button):
    global flap, game, tint
    if game == 3:
        if button == mouse.LEFT:
            flap = 2
    if game == 2:
        if button == mouse.LEFT and tint.collidepoint(pos):
            game = 3
    if game == 4:
        if button == mouse.LEFT and back.collidepoint(pos):
            game = 1
    if game == 2:
        if button == mouse.LEFT and back.collidepoint(pos):
            game = 1

def on_mouse_up(pos, button):
    global flap, game
    if game == 3:
        if button == mouse.LEFT:
            flap = 1
    if game == 1:
        if button == mouse.LEFT and play.collidepoint(pos):
            game = 2
        if button == mouse.LEFT and bhelp.collidepoint(pos):
            game = 4

def on_key_down(key):
    global flap, game
    if game == 3:
        if key == key.SPACE:
            flap = 2
        if key == key.ESCAPE:
            game = 4

def on_key_up(key):
    global flap, game
    if game == 3:
        if key == key.SPACE:
            flap = 1
        if key == key.SPACE:
            game = 3
