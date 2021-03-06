class Boss:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def calc_next(self, dx, dy):
        return (self.x + dx), (self.y + dy)

    def match(self, x, y):
        return self.x == x and self.y == y