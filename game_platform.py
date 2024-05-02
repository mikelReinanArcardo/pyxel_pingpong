import pyxel
import global_vars

class Platform:
    def __init__(self, speed):
        self.x = global_vars.WINDOW_WIDTH // 2 - 20
        self.y = global_vars.WINDOW_HEIGHT * .85
        self.speed = speed

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x >= 0:
            self.x += -self.speed if self.x >= self.speed else -self.x 
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x <= global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH:
            self.x += self.speed if self.x <= global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH - self.speed else global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH - self.x

    def draw(self):
        pyxel.rect(self.x, self.y, global_vars.PLATFORM_WIDTH, global_vars.PLATFORM_HEIGHT, 9)