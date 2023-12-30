import pgzrun

WIDTH = 500
HEIGHT = 500
import random

alien = Actor("alien")
alien.pos = (400, 50)
box = Rect((20, 20), (40, 40))
score = 0
speed = 5

def draw():
    screen.clear()
    screen.draw.filled_rect(box, "blue")
    alien.draw()

def update():
    global score
    if keyboard.right:
        alien.x = alien.x + 10
    elif keyboard.left:
        alien.x = alien.x - 10
    elif keyboard.up:
        alien.y = alien.y - 10
    elif keyboard.down:
        alien.y = alien.y + 10
    if alien.x > WIDTH:
        alien.x = 0
    if alien.x < 0:
        alien.x = WIDTH
    if alien.y > HEIGHT:
        alien.y = 0
    if alien.y < 0:
        alien.y = HEIGHT   
    if alien.colliderect(box):
        box.x = random.randint(0, WIDTH)
        box.y = random.randint(0, HEIGHT)
        score = score + 1
        print("Score:", score)

        if alien.x > WIDTH:
            alien.x = 0
        if alien.x < 0:
            alien.x = WIDTH
        if alien.y > HEIGHT:
            alien.y = 0
        if alien.y < 0:
            alien.y = HEIGHT


pgzrun.go()