from Balls import *
from typing import List
import arcade
import random

class MyBrick(arcade.Sprite):
    
    def __init__(self, health : int = 2, brick_x : int = 850, brick_y : int = 400, width : int = 64, height : int = 32):
        super().__init__(texture=None, scale=1.0)

        self.screen = MyScreen.GetScreen()

        self.texture = None

        self._health = health
        if self._health == 6: self.texture = arcade.load_texture("Images\png\element_grey_rectangle.png")

        self.width = width
        self.height = height

        self.center_x = brick_x
        self.center_y = brick_y

        self.set_sprite_scale()

#-------------------------------------------------------------------------------

    def update_texture(self):
        if self._health == 1: # Red
            self.texture = arcade.load_texture("Images\png\element_red_rectangle.png")
        elif self._health == 2: # Gold
            self.texture = arcade.load_texture("Images\png\element_yellow_rectangle.png")
        elif self._health == 3: # Green
            self.texture = arcade.load_texture("Images\png\element_green_rectangle.png")
        elif self._health == 4: # Blue
            self.texture = arcade.load_texture("Images\png\element_blue_rectangle.png")
        elif self._health == 5: # Purple
            self.texture = arcade.load_texture("Images\png\element_purple_rectangle.png")
        elif self._health == 6: # Gray
            self.texture = arcade.load_texture("Images\png\element_grey_rectangle.png")

    def draw(self):
        if self._health != 6: 
            self.update_texture()
        super().draw()

    def set_sprite_scale(self, scale_x : float = 1.0, scale_y : float = 1.0):
        self.scale_x = scale_x
        self.scale_y = scale_y

    def find_and_set_sprite_scale(self, width : int, height: int):
        self.set_sprite_scale(width / self.texture.width, height / self.texture.height)
    
    @classmethod
    def create_brick_map(cls, rows: int = 8):
        screen = MyScreen.GetScreen()
        start_y = screen.height - 32
        columns = screen.width // 64

        brick_map: List[MyBrick] = []

        for row in range(rows):
            for column in range(columns):
                health = random.randint(1, 6)
                brick_x = 58 + column * 64
                brick_y = start_y - row * 32

                brick_map.append(cls(health, brick_x, brick_y))

        return brick_map


#-------------------------------------------------------------------------------

    @property
    def health(self):
        return self._health

    @property
    def br_width(self):
        return self._width

    @property
    def br_height(self):
        return self._height

    @property
    def x(self):
        return self.center_x

    @property
    def y(self):
        return self.center_y

#-------------------------------------------------------------------------------

    @health.setter
    def health(self, value: int):
        self._health = value

    @x.setter
    def x(self, value: int):
        self.center_x = value

    @y.setter
    def y(self, value: int):
        self.center_y = value
