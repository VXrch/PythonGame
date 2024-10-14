import arcade
from Screen import *

class MyPlayer(arcade.Sprite):

    def __init__(self, width: int = 100, speed: int = 800, texture: str = "Images\png\element_purple_rectangle.png"):
        super().__init__(texture, scale=1.0)

        self._screen = MyScreen.GetScreen()
        self._speed = speed

        self.center_x = self._screen.width / 2
        self.center_y = 100

        self.health = 3

        self._right = False
        self._left = False

        self.width = width
        self.height = 24

#-------------------------------------------------------------------------------

    def move_right(self, delta_time: float):
        if self._right:
            new_x = self.center_x + self._speed * delta_time

            # check right border
            if new_x + self.width / 2 <= self._screen.width:
                self.center_x = new_x
            else:
                self.center_x = self._screen.width - self.width / 2 # set player to border

    def move_left(self, delta_time: float):
        if self._left:
            new_x = self.center_x - self._speed * delta_time

            # check left border
            if new_x - self.width / 2 >= 0:
                self.center_x = new_x
            else:
                self.center_x = self.width / 2  # set player to border

    def draw(self):
        super().draw()
        self.draw_hearts()

    def draw_hearts(self):
        heart_texture = arcade.load_texture("Images\png\heart.png")
        heart_size = 24 # px
        margin = 10 # space

        for i in range(self.health):
            x = self._screen.width - heart_size - (margin * (i * 3))
            y = heart_size + 10
            arcade.draw_texture_rectangle(x, y, heart_size, heart_size, heart_texture)


#-------------------------------------------------------------------------------

    @property
    def x(self): return self.center_x

    @property
    def y(self): return self.center_y

    @property
    def go_right(self): return self._right

    @property
    def go_left(self): return self._left

    @property
    def pl_width(self): return self.width

    @property
    def pl_height(self): return self.height

    @property
    def speed(self): return self._speed

#-------------------------------------------------------------------------------

    @go_left.setter
    def go_left(self, value: bool): self._left = value

    @go_right.setter
    def go_right(self, value: bool): self._right = value

    @x.setter
    def x(self, value: int): self._x = value

    @y.setter
    def y(self, value: int): self._y = value

    @pl_width.setter
    def pl_width(self, value: int): self._width = value

    @pl_height.setter
    def pl_height(self, value: int): self._height = value
    
    @speed.setter
    def speed(self, value: int): self.speed = value
