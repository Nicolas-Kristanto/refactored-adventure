from random import randint

score = 0

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

def draw():
    screen.clear()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10,600)

def place_orange():
    orange.x = randint(10,800)
    orange.y = randint(10,600)

def place_pineapple():
    pineapple.x = randint(10,800)
    pineapple.y = randint(10,600)

def on_mouse_down(pos):
    global score
    if apple.collidepoint(pos):
        print("Good shot!")
        score = score + 1
        place_apple()
        place_orange()
        place_pineapple()
    else:
        print("You missed!")
        score = score - 1
        place_apple()
        place_orange()
        place_pineapple()

place_apple()
place_orange()
place_pineapple()
