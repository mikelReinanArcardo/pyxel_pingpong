import pyxel
import global_vars
from random import random
from game_ball import Ball
from game_platform import Platform
from game_block import Block

class App:
    def __init__(self):
        pyxel.init(global_vars.WINDOW_WIDTH, global_vars.WINDOW_HEIGHT)
        self.startGame()
        pyxel.run(self.update, self.draw)

    def startGame(self, level=0):
        global_vars.score = 0
        pyxel.cls(1)
        self.platform = Platform()
        self.ball = Ball(self.platform)
        self.blocks: list[Block] = list()
        # Make game endless by adding progresion
        # Minimum Platform Speed: x
        # Maximum Ball Speed: y
        # Max no. of Blocks : 40
        num_of_blocks = level * 3 + 10
        blocks_pos = list()
        # Kinda slow? 
        for _ in range(num_of_blocks):
            block_coords = self.get_block_pos()

            while (self.collides_with_other_blocks(blocks_pos, block_coords)):
                block_coords = self.get_block_pos()

            blocks_pos.append(block_coords)
            self.blocks.append(Block(block_coords[0], block_coords[1], self.ball))

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

    def get_block_pos(self):
        xPos = min(10 + random() * global_vars.WINDOW_WIDTH, global_vars.WINDOW_WIDTH - 20) 
        yPos = min(10 + random() * (global_vars.WINDOW_HEIGHT / 2), global_vars.WINDOW_HEIGHT / 2 - 10)
        return (xPos, yPos)

    def collides_with_other_blocks(self, block_pos, curr_block):
        for block_x, block_y in block_pos:
            curr_block_x, curr_block_y = curr_block
            if abs(curr_block_x - block_x) <= global_vars.BLOCK_SIZE and abs(curr_block_y - block_y) <= global_vars.BLOCK_SIZE:
                return True
        return False

App()