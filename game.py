import pyxel

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 15
BALL_RADIUS = 5

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        self.platform = Platform()
        self.ball = Ball()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.platform.update()
        self.ball.update()

    def draw(self):
        pyxel.cls(1)
        self.platform.draw()
        self.ball.draw()

class Platform:
    def __init__(self):
        self.x = WINDOW_WIDTH // 2 - 20
        self.y = WINDOW_HEIGHT * .85

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x >= 0:
            self.x += -5 if self.x >= 5 else -self.x 
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x <= WINDOW_WIDTH - PLATFORM_WIDTH:
            self.x += 5 if self.x <= WINDOW_WIDTH - PLATFORM_WIDTH - 5 else WINDOW_WIDTH - PLATFORM_WIDTH - self.x

    def draw(self):
        pyxel.rect(self.x, self.y, PLATFORM_WIDTH, PLATFORM_HEIGHT, 9)

class Ball: 
    def __init__(self):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2

    def update(self):
        self.y += 1

    def draw(self):
        pyxel.circ(self.x, self.y, BALL_RADIUS, 4)

App()