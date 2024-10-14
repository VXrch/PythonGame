import arcade
import random
from Player import *

class Ball(arcade.Sprite):

    def __new__(cls, *args, **kwargs):
        if cls is Ball:
            raise TypeError("You can't create just a BALL!!! You must create a COLORED ball! \\(^.^)/")
        return super(Ball, cls).__new__(cls)

    def __init__(self, radius: int, color, damage: int, texture : str, speed: int = 150):
        super().__init__(texture, scale=1.0)

        self._screen = MyScreen.GetScreen()
        self._alive = True

        self.center_x = self._screen.width / 2
        self.center_y = 112

        self.change_x = speed
        self.change_y = speed
        
        self._radius = radius
        self._color = color

        self._damage = 1 if not (0 < damage <= 5) else damage

        self.update_scale()

#-------------------------------------------------------------------------------

    def update_scale(self):
        self.scale = self.radius * 2 / 22.0

    def set_radius(self, new_radius):
        self.radius = new_radius
        self.update_scale()

#-------------------------------------------------------------------------------

    def move(self, delta_time: float):

        self.center_x += self.change_x * delta_time 
        self.center_y += self.change_y * delta_time 

        if self.center_x >= self._screen.width - self.radius:
            self.change_dir('x')
            self.center_x = self._screen.width - self.radius

        if self.center_x <= self.radius:
            self.change_dir('x')
            self.center_x = self.radius

        if self.center_y >= self._screen.height - self.radius:
            self.change_dir('y')
            self.center_y = self._screen.height - self.radius

        if self.center_y <= self.radius:
            self.change_dir('y')
            self.center_y = self.radius

    def change_dir(self, prop:str = 'full'):
        if prop == 'y': self.change_y *= -1
        elif prop == 'x': self.change_x *= -1
        else:        
            self.change_x *= -1
            self.change_y *= -1

        if self.center_y < 0 + self.radius: 
            self._alive = False

    def draw(self):
        super().draw()

    def reset_position(self, player : MyPlayer):
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height / 2 + self.height / 2
        self.change_x = random.randint(10, 200)
        self.change_y = random.randint(10, 200)

#-------------------------------------------------------------------------------

    @property
    def x(self): return self.center_x

    @property
    def y(self): return self.center_y

    @property
    def speed_x(self): return self.change_x

    @property
    def speed_y(self): return self.change_y

    @property
    def radius(self): return self._radius

    @property
    def color(self): return self._color

    @property
    def damage(self): return self._damage

    @property
    def alive(self): return self._alive

#-------------------------------------------------------------------------------

    @speed_x.setter
    def speed_x(self, value: int): self.change_x = value

    @speed_y.setter
    def speed_y(self, value: int): self.change_y = value
        
    @damage.setter
    def damage(self, value: int): self._damage = value

################################################################################

class BlueBall(Ball):

    def __init__(self):
        texture = "Images\png\BlueBall.png"
        super().__init__(12, arcade.color.BLUE, 1, texture, 150)


class RedBall(Ball):

    def __init__(self):
        texture = "Images\png\RedBall.png"
        super().__init__(16, arcade.color.RED, 2, texture, 260)

class GoldBall(Ball):

    def __init__(self):
        texture = "Images\png\GoldBall.png"
        super().__init__(10, arcade.color.GOLD, 3, texture, 310)

class BlackBall(Ball):

    def __init__(self):
        texture = "Images\png\BlackBall.png"
        super().__init__(20, arcade.color.BLACK, 4, texture, 150)
