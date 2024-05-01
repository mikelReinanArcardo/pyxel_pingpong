import pyxel

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
PLATFORM_WIDTH = 60
PLATFORM_HEIGHT = 15

class App:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT)
        
        self.platform = Platform()

        pyxel.run(self.update, self.draw)

    def update(self):
        self.platform.update()

    def draw(self):
        pyxel.cls(1)
        self.platform.draw()

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

App()