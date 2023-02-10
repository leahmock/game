cat = Actor("character")
cat.topright = 0, 10

WIDTH = 500
HEIGHT = cat.height + 20


def draw():
    screen.fill((128, 0, 0))
    cat.draw()


def update():
    cat.left = cat.left + 2
    if cat.left > WIDTH:
        cat.right = 0


def on_mouse_down(pos):
    if cat.collidepoint(pos):
        set_cat_hurt()


def set_cat_hurt():
    cat.image = "character_clicked"
    clock.schedule_unique(set_cat_normal, 1.0)


def set_cat_normal():
    cat.image = "character"
