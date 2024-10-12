from arcade import color

class MyScreen():

    _instance = None
    _initialized = False

    _width = 1200
    _height = 720

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = super(MyScreen, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, width=1200, height=720):
        if not MyScreen._initialized:
            self._instance.width = width
            self._instance.height = height
            MyScreen._initialized = True

#-------------------------------------------------------------------------------

    @classmethod
    def GetScreen(cls):
        if cls._instance is None:
            cls._instance = MyScreen()
        return cls._instance

#-------------------------------------------------------------------------------

    @property
    def get_width(self):
        return self._width

    @property
    def get_height(self):
        return self._height
    