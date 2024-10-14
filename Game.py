import arcade
import random
from typing import Type
from typing import Union
from typing import List
from Brick import *

class MyGame(arcade.Window):
    
    def __init__(self, title):
        
        self._screen = MyScreen.GetScreen()
        super().__init__(self._screen.width, self._screen.height, title)

        arcade.set_background_color(arcade.color.ALMOND)
        self.set_location(160, 70)

        self.game_end = 'no'
        
        self._balls : List[Type[Ball]] = []
        self._bricks : List[MyBrick] = []
        self._player = MyPlayer()

        self.add_ball(BlueBall())
        self.add_bricks_list(MyBrick.create_brick_map(10))

#-------------------------------------------------------------------------------

    def on_draw(self):
        arcade.start_render()

        if self.game_end != 'no':
            self.game_over()
        else:
            for brick in self._bricks:
                brick : MyBrick
                brick.draw()

            self._player.draw()

            for ball in self._balls:
                ball : Type[Ball]
                ball.draw()

    def on_update(self, delta_time: float):

        if self.check_game_is_end(): return

        for ball in self._balls:
            ball : Type[Ball]
            if ball.alive: ball.move(delta_time)
            else: self.rm_ball(ball)

        self.check_for_collusion()

        if self._player.go_left: self._player.move_left(delta_time)
        if self._player.go_right: self._player.move_right(delta_time)

#-------------------------------------------------------------------------------

    def ball_brick_collision(self, ball: Type[Ball], brick: Union[Ball, MyPlayer]):
        
        # borders of the brick/player
        brick_left = brick.center_x - brick.width / 2
        brick_right = brick.center_x + brick.width / 2
        brick_top = brick.center_y + brick.height / 2
        brick_bottom = brick.center_y - brick.height / 2

        # borders of the ball
        ball_left = ball.center_x - ball.radius
        ball_right = ball.center_x + ball.radius
        ball_top = ball.center_y + ball.radius
        ball_bottom = ball.center_y - ball.radius

        # where was the collusion
        if ball_right >= brick_left and ball_left <= brick_right:
            # vertikal collusion
            if ball_bottom < brick_top and ball_top > brick_bottom:
                # down
                ball.change_dir('y')
            elif ball_top > brick_bottom and ball_bottom < brick_top:
                # up
                ball.change_dir('y')

        elif ball_top >= brick_bottom and ball_bottom <= brick_top:
            # horizontal collusion
            if ball_right > brick_left and ball_left < brick_left:
                # left
                ball.change_dir('x')
            elif ball_left < brick_right and ball_right > brick_right:
                # right
                ball.change_dir('x')
        
        if isinstance(brick, MyBrick):
            if brick.health - ball.damage > 0:
                brick.health -= ball.damage
            else:
                self.rm_brick(brick)


    def check_for_collusion(self): 

        for ball in self._balls:
            ball : Type[Ball]
            for brick in self._bricks:
                brick : MyBrick

                if arcade.check_for_collision(ball, brick): 
                    self.ball_brick_collision(ball, brick)

        for ball in self._balls:
            ball : Type[Ball]
            if arcade.check_for_collision(ball, self._player):
                ball.change_x += 5
                self.ball_brick_collision(ball, self._player)

#-------------------------------------------------------------------------------

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT: self._player.go_right = True
        if symbol == arcade.key.LEFT: self._player.go_left = True  
        if symbol == arcade.key.ESCAPE: self.close()      

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.RIGHT: self._player.go_right = False
        if symbol == arcade.key.LEFT: self._player.go_left = False

#-------------------------------------------------------------------------------

    def drop_ball_if_possible(self, brick: MyBrick):

        if len(self._balls) >= 3:  # max 3 balls!
            return None

        damage = random.randint(2, 4)

        if damage == 4: chance = 20     # 10%
        elif damage == 3: chance = 30   # 20%
        elif damage == 2: chance = 40   # 30%

        if random.randint(0, 100) < chance:
            # damage = ball
            if damage == 4:
                new_ball = BlackBall()
            elif damage == 3:
                new_ball = GoldBall()
            elif damage == 2:
                new_ball = RedBall()

            # set pos. to broken brick
            new_ball.center_x = brick.center_x
            new_ball.center_y = brick.center_y

            return new_ball
        else:
            return None

# -------------

    def add_ball(self, ball : Type[Ball]):
        self._balls.append(ball)

    def add_balls_list(self, balls_list):
        if all(isinstance(ball, Ball) for ball in self._balls):
            self._balls.extend(balls_list)

    def rm_ball(self, ball : Type[Ball]):
        ball.kill()
        self._balls.remove(ball)

# -------------

    def add_brick(self, brick : MyBrick):
        self._bricks.append(brick)
    
    def add_bricks_list(self, bricks_list):
        if all(isinstance(brick, MyBrick) for brick in self._bricks):
            self._bricks.extend(bricks_list) 

    def rm_brick(self, brick : MyBrick):

        new_ball : Type[Ball] = self.drop_ball_if_possible(brick)
        if new_ball:
            self._balls.append(new_ball)
        
        brick.kill()
        self._bricks.remove(brick)


#-------------------------------------------------------------------------------

    def blue_ball_exist(self):
        for ball in self._balls:
            if isinstance(ball, BlueBall): 
                return True
        return False

    def bricks_to_beat_exist(self):
        for brick in self._bricks:
            if brick.health != 6: 
                return True
        return False

#-------------------------------------------------------------------------------

    def check_game_is_end(self):
        
        if not self.blue_ball_exist(): 
            
            self._player.health -= 1
            if self._player.health == 0:
                self.game_end = 'loose'
                return True
            else: 
                self.add_ball(BlueBall())
                for ball in self._balls:
                    ball : BlueBall
                    ball.reset_position(self._player)
        
        if not self.bricks_to_beat_exist(): 
            self.game_end = 'win'
            return True

    def game_over(self):
        arcade.set_background_color(arcade.color.BLACK)
        
        if self.game_end == 'win':
                    arcade.draw_text("(/^.^)/ ~ ~ ~ YOU WIN ~ ~ ~ \\(^.^\\)", 
            self._screen.width // 4, self._screen.height // 2, 
            arcade.color.WHITE, font_size=14, 
            anchor_x="center", anchor_y="center")

        else:
            arcade.draw_text("/(v_v)\\ - - - YOU LOOSE - - - /(v_v)\\", 
                self._screen.width // 4, self._screen.height // 2, 
                arcade.color.WHITE, font_size=14, 
                anchor_x="center", anchor_y="center")


################################################################################

MyGame("Game")
arcade.run()