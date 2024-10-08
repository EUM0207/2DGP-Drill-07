import random
from pico2d import *

# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400,30)
    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('run_animation.png')
    def update(self):
        self.frame = random.randint(0, 7)
        self.x += 5
    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = 0
        self.image = load_image('ball21x21.png')
        self.z = random.randint(1, 10)
    def update(self):
         if self.y > 60:
            self.y -= self.z
    def draw(self):
        self.image.draw(self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(0, 700), 599
        self.frame = 0
        self.image = load_image('ball41x41.png')
        self.z = random.randint(1, 10)
    def update(self):
        if self.y > 70:
            self.y -= self.z
    def draw(self):
        self.image.draw(self.x, self.y)





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def update_world():
    grass.update()
    #boy.update()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

def render_world():
    clear_canvas()

    grass.draw()
    #boy.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()

    update_canvas()

def reset_world():
    global running
    global grass
    #global boy
    global team
    global balls

    running = True
    grass = Grass() # Grass 클래스를 이용해서 grass 객체를 생성
    #boy = Boy()
    team = [Boy() for i in range(11)]
    balls = [random.choice([SmallBall,BigBall])() for i in range(20)]


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
