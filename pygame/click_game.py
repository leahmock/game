import random

cat = Actor("character")
cat.topright = 0, 10

WIDTH = 500
HEIGHT = 300
speed = 1

def draw():
    screen.fill((128, 0, 0))
    cat.draw()

def update():
    global speed
    cat.right = cat.right + speed
    cat.top = cat.top + speed
    if cat.right > WIDTH:
        cat.left = 0
    if cat.top > HEIGHT:
        cat.bottom = 0

def on_mouse_down(pos):
    global speed
    if cat.collidepoint(pos):
        set_cat_hurt()
        sounds.ping.play()
        random_cat_pos()
        speed = random.randrange(-5, 5, step=1)
    else:
        sounds.bing.play()

def random_cat_pos():
    cat.x = random.randrange(0, 500, step=1)
    cat.y = random.randrange(0, 300, step=1)
    cat.right = cat.right + random.randrange(50, 100, step=1)

def set_cat_hurt():
    cat.image = "character_clicked"
    clock.schedule_unique(set_cat_normal, 0.5)


def set_cat_normal():
    cat.image = "character"

