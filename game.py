import pyxel
import global_vars
from game_ball import Ball
from game_platform import Platform
from game_block import Block

class App:
    def __init__(self):
        pyxel.init(global_vars.WINDOW_WIDTH, global_vars.WINDOW_HEIGHT)
        self.startGame()
        pyxel.run(self.update, self.draw)

    def startGame(self):
        global_vars.score = 0
        pyxel.cls(1)
        self.platform = Platform()
        self.ball = Ball(self.platform)
        self.blocks: list[Block] = list()
        for i in range(10):
            self.blocks.append(Block(i*10 + i*20 + 10, 30, self.ball))

    def update(self):
        if global_vars.play:
            self.platform.update()
            self.ball.update()
            for block in self.blocks:
                if block.collide_with_ball():
                    self.blocks.remove(block)
                    global_vars.score += 1
        else:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.startGame()
                global_vars.play = True
                global_vars.lost = False

    def draw(self):
        pyxel.cls(1)
        if not global_vars.play:
            pyxel.text(global_vars.WINDOW_WIDTH * .38, global_vars.WINDOW_HEIGHT * .4, "Press SPACE to play", 7)
        if global_vars.lost:
            pyxel.text(global_vars.WINDOW_WIDTH * .435, global_vars.WINDOW_HEIGHT * .35, "Game Over!", 7)
        pyxel.text(global_vars.WINDOW_WIDTH * .85, global_vars.WINDOW_HEIGHT * .025, f"Score: {global_vars.score}", 7)
        self.platform.draw()
        self.ball.draw()
        for block in self.blocks:
            block.draw()

App()