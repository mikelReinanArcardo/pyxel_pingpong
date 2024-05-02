import pyxel
import global_vars

class Ball: 
    def __init__(self, platform, speed):
        self.x = global_vars.WINDOW_WIDTH // 2
        self.y = global_vars.WINDOW_HEIGHT // 2
        self.xDirection = 0
        self.yDirection = 1
        self.top = self.y - global_vars.BALL_RADIUS
        self.bot = self.y + global_vars.BALL_RADIUS
        self.right = self.x + global_vars.BALL_RADIUS
        self.left = self.x - global_vars.BALL_RADIUS
        self.speed = speed
        self.platform = platform

    def update(self):
        self.x += self.speed * self.xDirection
        self.y += self.speed * self.yDirection
        self.top = self.y - global_vars.BALL_RADIUS
        self.bot = self.y + global_vars.BALL_RADIUS
        self.right = self.x + global_vars.BALL_RADIUS
        self.left = self.x - global_vars.BALL_RADIUS
        self.collide_border()
        self.collide_with_platform()

    def draw(self):
        pyxel.circ(self.x, self.y, global_vars.BALL_RADIUS, 4)

    def collide_border(self):
        if self.top <= 0:
            self.yDirection = 1
        if self.left <= 0:
            self.xDirection = 1
        if self.right >= global_vars.WINDOW_WIDTH:
            self.xDirection = -1
        if self.bot >= global_vars.WINDOW_HEIGHT:
            global_vars.play = False
            global_vars.lost = True

    def collide_with_platform(self):
        offset = global_vars.PLATFORM_WIDTH // 2
        platform_center = self.platform.x + offset
        platform_top = self.platform.y 
        if ((self.x <= self.platform.x + global_vars.PLATFORM_WIDTH and self.x >= self.platform.x) and (self.bot >= platform_top and self.top <= platform_top + global_vars.PLATFORM_HEIGHT)):
            self.yDirection *= -1
            numerator = (self.x - platform_center)
            self.xDirection = numerator / offset if numerator < offset else 1