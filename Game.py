import arcade
import arcade.color
from typing import Type
from Brick import *

class MyGame(arcade.Window):
    
    def __init__(self, title):
        
        self._screen = MyScreen.GetScreen()
        super().__init__(self._screen.get_width, self._screen.get_height, title)

        self.set_location(120, 70)
        
        self._balls = []
        self._bricks = []
        self._player = MyPlayer()

    def on_draw(self):
        arcade.start_render()

        for brick in self._bricks:
            brick : MyBrick
            brick.draw()

        self._player.draw()

        for ball in self._balls:
            ball : Type[Ball]
            ball.draw()
        

    def on_update(self, delta_time: float):
        
        for ball in self._balls:
            ball : Type[Ball]
            ball.move()

        self.check_for_collusion() 

        if self._player.go_left: self._player.move_left(delta_time)
        if self._player.go_right: self._player.move_right(delta_time)

    def check_for_collusion(self):
        for ball in self._balls:
            ball : Type[Ball]
            for brick in self._bricks:
                brick : MyBrick
                if arcade.check_for_collision(ball, brick): 
                    if brick.health - ball.damage == 0: # Если они ушли в ноль, мяч отпрыгнет, а плитка сломаеться
                        brick.alive = False
                        ball.jump = True
                        ball.damage = 0
                    elif brick.health - ball.damage > 0: # Если хп больше чем дамаг, то мяч отпрыгнет, а хп уменьшиться
                        brick.health = brick.health - ball.damage
                        ball.jump = True
                        ball.damage = 0
                    elif brick.health - ball.damage < 0: # Если дамаг был больше чем хп, то плитка сломаеться, а мяч полетит дальше с меньшей силой
                        brick.alive = False
                        ball.damage = ball.damage - brick.health

    def on_key_press(self, symbol: int, modifires: int):
        if symbol == arcade.key.RIGHT: self._player.go_right = True
        if symbol == arcade.key.LEFT: self._player.go_left = True        

    def on_key_release(self, symbol: int, modifires: int):
        if symbol == arcade.key.RIGHT: self._player.go_right = False
        if symbol == arcade.key.LEFT: self._player.go_left = False

    def add_ball(self, ball: Type[Ball]):
        self._balls.append(ball)
    
    def add_brick(self, brick: MyBrick):
        self._bricks.append(brick)


MyGame("Game")
arcade.run()