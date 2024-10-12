import arcade.color
from Screen import *

class Ball:

    def __new__(cls, *args, **kwargs):
        if cls is Ball:
            raise TypeError("You can't create just a BALL!!! You must create a COLORED ball! \\(^.^)/")
        return super(Ball, cls).__new__(cls)

    def __init__(self, speed: int, radius: int, color, strength: int):

        self._screen = MyScreen.GetScreen()

        self._x = self._screen.get_width / 2
        self._y = 112
        self._speed_x = speed
        self._speed_y = speed
        self._radius = radius
        self._color = color
        self._strength = 1 if not (0 < strength <= 5) else strength

        self._damage = self._strength
        self._jump = False

    def move(self, delta_time: float):
        self._x += self._speed_x * delta_time 
        self._y += self._speed_y * delta_time 

        if self._x >= 1280 - self._radius or self._x <= 0 + self._radius:
            self._speed_x *= -1
        if self._y >= 700 - 10 or self._y <= 0 + 10:
            self._speed_y *= -1

    def draw(self):
        pass

#-------------------------------------------------------------------------------

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def speed_x(self): return self._speed_x

    @property
    def speed_y(self): return self._speed_y

    @property
    def radius(self): return self._radius

    @property
    def color(self): return self._color

    @property
    def strength(self): return self._strength

    @property
    def damage(self): return self._damage

    @property
    def jump(self): return self._jump

#-------------------------------------------------------------------------------

    @speed_x.setter
    def speed_x(self, value: int): self._speed_x = value

    @speed_y.setter
    def speed_y(self, value: int): self._speed_y = value
        
    @damage.setter
    def damage(self, value: int): self._damage = value

    @jump.setter
    def jump(self, value: bool): self._jump = value

################################################################################

class RedBall(Ball):

    def __init__(self):
        super().__init__(200, 5, arcade.color.RED, 2)

class BlueBall(Ball):

    def __init__(self):
        super().__init__(100, 10, arcade.color.BLUE, 1)

class GoldBall(Ball):

    def __init__(self):
        super().__init__(150, 5, arcade.color.GOLD, 3)

class BlackBall(Ball):

    def __init__(self):
        super().__init__(70, 15, arcade.color.BLACK, 5)
