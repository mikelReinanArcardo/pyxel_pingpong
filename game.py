import pyxel

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 15
BALL_RADIUS = 7

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        self.platform = Platform()
        self.ball = Ball(self.platform)

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
    def __init__(self, platform):
        self.x = WINDOW_WIDTH // 2
        self.y = WINDOW_HEIGHT // 2
        self.xDirection = 0
        self.yDirection = 1
        self.top = self.y - BALL_RADIUS
        self.bot = self.y + BALL_RADIUS
        self.right = self.x + BALL_RADIUS
        self.left = self.x - BALL_RADIUS
        self.platform: Platform = platform

    def update(self):
        self.x += 5 * self.xDirection
        self.y += 5 * self.yDirection
        self.top = self.y - BALL_RADIUS
        self.bot = self.y + BALL_RADIUS
        self.right = self.x + BALL_RADIUS
        self.left = self.x - BALL_RADIUS
        self.collide_border()
        self.collide_with_platform()

    def draw(self):
        pyxel.circ(self.x, self.y, BALL_RADIUS, 4)

    def collide_border(self):
        if self.top <= 0:
            self.yDirection = 1
        if self.bot >= WINDOW_HEIGHT:
            self.yDirection = -1
        if self.left <= 0:
            self.xDirection = 1
        if self.right >= WINDOW_WIDTH:
            self.xDirection = -1

    def collide_with_platform(self):
        platform_center = self.platform.x  + PLATFORM_WIDTH // 2
        platform_top = self.platform.y 
        if ((self.x <= self.platform.x + PLATFORM_WIDTH and self.x >= self.platform.x) and (self.bot >= platform_top and self.top <= platform_top + PLATFORM_HEIGHT)):
            self.yDirection *= -1
            self.xDirection = (self.x - platform_center) / (PLATFORM_WIDTH // 2)

App()