from random import randint

WIDTH = 750
HEIGHT = 750
score = 0
game_over = False
canary_counter = 0

canary = Actor("canary")
canary.pos = 100, 100

worm = Actor("worm")
worm.pos = 200, 200

evilcanary = Actor("evilcanary")
evilcanary.pos = 300, 300


def draw():
    screen.fill((111, 174, 255))
    canary.draw()
    worm.draw()
    evilcanary.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

    if game_over:
        screen.fill("black")
        screen.draw.text(
            "Final Score: " + str(score), color="white", topleft=(10, 10), fontsize=60
        )


def place_worm():
    worm.x = randint(20, (WIDTH - 20))
    worm.y = randint(20, (HEIGHT - 20))


def place_evilcanary():
    evilcanary.x = randint(40, (WIDTH - 40))
    evilcanary.y = randint(40, (HEIGHT - 40))


def time_up():
    global game_over
    game_over = True


def update():
    global canary_counter
    global score

    if keyboard.left:
        canary.x = canary.x - 2
        canary_counter = canary_counter + 5
    elif keyboard.right:
        canary.x = canary.x + 2
        canary_counter = canary_counter + 5
    elif keyboard.up:
        canary.y = canary.y - 2
        canary_counter = canary_counter + 5
    elif keyboard.down:
        canary.y = canary.y + 2
        canary_counter = canary_counter + 5

    worm_collected = canary.colliderect(worm)
    if worm_collected:
        score = score + 10
        set_canary_happy()
        place_worm()

    canary_collide = canary.colliderect(evilcanary)
    if canary_collide:
        score = score - 10
        set_canary_sad()
        place_evilcanary()

    if canary_counter == 300:
        place_evilcanary()
        canary_counter = 0

def set_canary_happy():
    canary.image = "happycanary"
    clock.schedule_unique(set_canary_normal, 1.0)

def set_canary_sad():
    canary.image = "sadcanary"
    clock.schedule_unique(set_canary_normal, 1.0)

def set_canary_normal():
    canary.image = "canary"

clock.schedule(time_up, 60.0)
place_worm()
place_evilcanary()
