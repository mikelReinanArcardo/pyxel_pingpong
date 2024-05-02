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

    def startGame(self, level=global_vars.level):
        pyxel.cls(1)
        self.platform = Platform()
        self.ball = Ball(self.platform)
        self.blocks: list[Block] = list()
        # Make game endless by adding progresion
        # Minimum Platform Speed: x
        # Maximum Ball Speed: y
        # Max no. of Blocks : 40
        num_of_blocks = min(level * 3 + 10, 40)
        blocks_pos = list()
        for _ in range(num_of_blocks):
            block_coords = self.get_block_pos()

            while (self.collides_with_other_blocks(blocks_pos, block_coords)):
                new_coords = self.get_block_pos()
                block_coords = new_coords

            blocks_pos.append(block_coords)
            self.blocks.append(Block(block_coords[0], block_coords[1], self.ball))

    def update(self):
        if global_vars.play:
            if (not self.blocks):
                global_vars.level += 1
                global_vars.play = False
            self.platform.update()
            self.ball.update()
            for block in self.blocks:
                if block.collide_with_ball():
                    self.blocks.remove(block)
                    global_vars.score += 1

        elif pyxel.btn(pyxel.KEY_SPACE):
            if global_vars.lost:
                self.startGame()
                global_vars.level = 0
                global_vars.score = 0
                global_vars.play = True
                global_vars.lost = False
            else: 
                self.startGame(global_vars.level)
                global_vars.play = True

    def draw(self):
        pyxel.cls(1)
        if not global_vars.play:
            if global_vars.level > 0 and not global_vars.lost:
                pyxel.text(global_vars.WINDOW_WIDTH * .35, global_vars.WINDOW_HEIGHT * .35, "Ready for the next round?", 7)
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