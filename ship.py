import random


class ship():
    def __init__(self, x, y, parent, speed):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 25
        self.speed = speed
        self.color = 'green'
        self.parent = parent

    def draw(self, canvas):
        canvas.create_rectangle(
            self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)
        canvas.create_rectangle(self.x + self.width / 2 - 5, self.y, self.x +
                                self.width / 2 + 5, self.y - self.height, fill=self.color)


class Shot():
    def __init__(self, x, y, parent):
        self.x = x
        self.y = y
        self.parent = parent
        self.width = 10
        self.height = 30
        self.color = 'orange'
        self.speed = 10

    def draw(self, canvas, i):
        if self.y >= 0:
            canvas.create_rectangle(
                self.x, self.y, self.x + 10, self.y - 20, fill=self.color)
            self.y -= self.speed
        if self.y < 0:
            self.parent.shots.remove(i)
        if self.y <= self.parent.invader_y + self.parent.invader.height and self.x >= self.parent.invader_x and self.x <= self.parent.invader_x + self.parent.invader.width:
            self.parent.magazine += 1
            self.parent.shots.remove(i)
            self.parent.invader_x = random.randint(
                0, self.parent.width-self.parent.invader.width)
            self.parent.invader_y = 0
            self.parent.score += 1
            self.parent.invader.speed = random.randint(1, 7)
