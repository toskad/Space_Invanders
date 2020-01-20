from tkinter import *
from ship import *
from invader import *
from dialogs import *
import csv
from operator import itemgetter


class MyApp:
    def __init__(self, parent):
        self.bg_color = 'black'
        self.width = 1000
        self.height = 800
        self.x = self.width/2-25
        self.y = self.height-130
        self.invader_x = self.width/2-25
        self.invader_y = 0
        self.parent = parent
        self.ship = None
        self.invader = None
        self.shot = None
        self.shots = []
        self.magazine = 3
        self.score = 0
        self.name = "Player"
        self.draw_widgets()
        self.redraw_canvas()

    def draw_widgets(self):
        self.canvas = Canvas(self.parent, width=self.width,
                             height=self.height-100, bg=self.bg_color)
        self.canvas.bind_all('<Key>', self.move_ship)
        self.canvas.pack()
        self.ship = ship(self.x, self.y, self, 10)
        self.invader = invader(self.invader_x, self.invader_y, self, 0)
        self.canvas.focus_set()

        menu = Menu(self.parent)
        self.parent.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label='Hra', menu=filemenu)
        filemenu.add_command(label='Nová Hra', command=self.reset)
        filemenu.add_command(label='Konec', command=self.parent.destroy)
        filemenu.add_command(label='Parametry objektu',
                             command=self.object_params)

        dialog = SetName(self.parent, self)
        self.parent.wait_window(dialog.top)

    def save_score(self):

        with open('scores.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow((self.name, str(self.score)))

        i = self.height/3+200

        with open('scores.csv', 'r') as file:
            score_list = list(csv.reader(file))
            res = sorted(score_list, key=itemgetter(1), reverse=True)
            for row in res:
                self.canvas.create_text(self.width/2, i,
                                        fill="white", font="helvetica 20", text=row)
                i += 50

    def object_params(self):
        dialog = SettingsDialog(self.parent, self, self.ship)
        self.parent.wait_window(dialog.top)
        self.redraw_canvas()

    def clear_canvas(self):
        self.canvas.delete("all")

    def game_over(self):
        self.clear_canvas()
        self.canvas.create_text(self.width/2, self.height/4,
                                fill="white", font="helvetica 60", text="Game Over")
        self.canvas.create_text(self.width/2, self.height/3, fill="white",
                                font="helvetica 20", text=f"Score: %s" % self.score)
        self.canvas.create_text(self.width/2, self.height/3+150,
                                fill="white", font="helvetica 40", text="Leader Board:")
        self.save_score()

    def reset(self):
        self.x = self.width/2-25
        self.y = self.height-130
        self.invader_x = self.width/2-25
        self.invader_y = 0
        self.magazine = 3
        self.score = 0
        self.ship = ship(self.x, self.y, self, self.ship.speed)
        self.invader = invader(self.invader_x, self.invader_y, self, 0)
        self.shots = []
        self.redraw_canvas()

    def redraw_canvas(self):
        self.clear_canvas()
        self.ship.draw(self.canvas)
        if self.invader_y <= self.y:
            self.invader_y += self.invader.speed
            self.invader = invader(
                self.invader_x, self.invader_y, self, self.invader.speed)
            self.invader.draw(self.canvas)
            for i in self.shots:
                i.draw(self.canvas, i)
            self.canvas.create_text(
                37, 20, fill="white", font="helvetica 12", text=f"Score: %s" % self.score)
            self.canvas.create_text(
                50, 40, fill="white", font="helvetica 12", text=f"Magazine: %s" % self.magazine)
            root.after(20, self.redraw_canvas)
        else:
            self.game_over()

    def move_ship(self, event):
        if event.keysym == "Up":
            if self.magazine != 0:
                self.shots.append(Shot(
                    self.ship.x + self.ship.width / 2 - 5, self.ship.y - self.ship.height, self))
                self.magazine -= 1

        elif event.keysym == "Left":
            if self.ship.x >= 0 + self.ship.speed:
                self.ship.x -= self.ship.speed

        elif event.keysym == "Right":
            if self.ship.x <= self.width - self.ship.width - self.ship.speed:
                self.ship.x += self.ship.speed


root = Tk()
root.resizable(width=False, height=False)
myapp = MyApp(root)
root.mainloop()
