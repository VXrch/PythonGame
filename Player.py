from Balls import *

class MyPlayer:

    def __init__(self, width: int = 100, speed: int = 50):

        self._screen = MyScreen.GetScreen()

        self._player_x = self._screen.get_width / 2
        self._player_y = 100
        self._player_speed = speed
        self._right = False
        self._left = False

        self._player_width = width
        self._player_height = 24

    def move_right(self, delta_time: float):
        self._player_x += self._player_speed * delta_time

    def move_left(self, delta_time: float):
        self._player_x -= self._player_speed * delta_time

    def draw(self):
        pass

#-------------------------------------------------------------------------------

    @property
    def player_x(self): return self._player_x

    @property
    def player_y(self): return self._player_y

    @property
    def player_speed(self): return self._player_speed

    @property
    def go_right(self): return self._right

    @property
    def go_left(self): return self._left

    @property
    def player_width(self): return self._player_width

    @property
    def player_height(self): return self._player_height

#-------------------------------------------------------------------------------

    @go_left.setter
    def go_left(self, value: bool): self._left = value

    @go_right.setter
    def go_right(self, value: bool): self._right = value

    @player_x.setter
    def player_x(self, value: int): self._player_x = value

    @player_y.setter
    def player_y(self, value: int): self._player_y = value

    @player_width.setter
    def player_width(self, value: int): self._player_width = value
    
    @player_speed.setter
    def player_speed(self, value: int): self._player_speed = value

    @player_height.setter
    def player_height(self, value: int): self._player_height = value
