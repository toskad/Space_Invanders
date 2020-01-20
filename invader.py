class invader():
    def __init__(self, x, y, parent, speed):
        self.x = x
        self.y = y
        self.parent = parent
        self.width = 50
        self.height = 40
        self.speed = speed
        self.points = [self.x, self.y, self.x+self.width,
                       self.y, self.x+self.width/2, self.y+self.height]

    def draw(self, canvas):
        canvas.create_polygon(self.points, fill='red')
