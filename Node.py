class Node():
    """Node Init"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.h = 0
        self.g = 0
        self.f = 0
