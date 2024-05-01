import pyxel
import global_vars

class Block:
    def __init__(self, x, y, ball):
        self.x = x
        self.y = y
        self.ball = ball

    def draw(self):
        pyxel.rect(self.x, self.y, global_vars.BLOCK_SIZE, global_vars.BLOCK_SIZE, 11)

    def collide_with_ball(self):
        offset = global_vars.BLOCK_SIZE // 2
        block_center = self.x + (offset)
        if (self.ball.top <= self.y + global_vars.BLOCK_SIZE and self.ball.bot >= self.y) and (self.ball.right >= self.x and self.ball.left <= self.x + global_vars.BLOCK_SIZE):
            self.ball.yDirection *= -1
            numerator = (self.ball.x - global_vars.BALL_RADIUS - block_center)
            self.ball.xDirection = numerator / (offset) if abs(numerator) < offset else 1
            return True
        return False