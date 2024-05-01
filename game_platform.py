import pyxel
import global_vars

class Platform:
    def __init__(self):
        self.x = global_vars.WINDOW_WIDTH // 2 - 20
        self.y = global_vars.WINDOW_HEIGHT * .85

    def update(self):
        if pyxel.btn(pyxel.KEY_LEFT) and self.x >= 0:
            self.x += -5 if self.x >= 5 else -self.x 
        if pyxel.btn(pyxel.KEY_RIGHT) and self.x <= global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH:
            self.x += 5 if self.x <= global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH - 5 else global_vars.WINDOW_WIDTH - global_vars.PLATFORM_WIDTH - self.x

    def draw(self):
        pyxel.rect(self.x, self.y, global_vars.PLATFORM_WIDTH, global_vars.PLATFORM_HEIGHT, 9)