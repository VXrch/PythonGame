from Player import *

class MyBrick:
    
    def __init__(self, health, color : arcade.color, brick_x : int, brick_y : int):

        self._health = health
        self._color = color
        self._width = 100
        self._height = 50

        self._alive = True

        self._x = brick_x
        self._y = brick_y

    def draw(self):
        pass

#-------------------------------------------------------------------------------

    @property
    def health(self):
        return self._health

    @property
    def alive(self):
        return self._alive

    @property
    def color(self):
        return self._color

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

#-------------------------------------------------------------------------------

    @health.setter
    def health(self, value: int):
        self._health = value
        if self.health <= 0: self._alive = False

    @color.setter
    def color(self, value: arcade.color):
        self._color = value

    @x.setter
    def x(self, value: int):
        self._x = value

    @y.setter
    def y(self, value: int):
        self._y = value

    @alive.setter
    def alive(self, value):
        self._alive = value