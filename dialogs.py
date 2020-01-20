from tkinter import *


class SettingsDialog:
    def __init__(self, parent, app, ship):
        self.ship = ship
        self.app = app
        top = self.top = Toplevel(parent)
        top.title("Settings:")
        top.transient(parent)
        top.grab_set()
        top.focus_set()
        x = parent.winfo_x()
        y = parent.winfo_y()
        top.geometry("%dx%d+%d+%d" % (400, 200, x+200, y+100))
        ship_speed = StringVar()
        ship_speed.set(self.ship.speed)
        label1 = Label(top, text="Settings", pady=5)
        label1.pack()

        container1 = Frame(top, width=400, pady=10, padx=10)

        label_ship = Label(container1, text="ship speed:")
        label_ship.pack()

        self.spinbox_ship = Spinbox(
            container1, from_=1, to=20, textvariable=ship_speed)
        self.spinbox_ship.pack(padx=10)

        container1.pack(fill=BOTH)

        button_ok = Button(top, text="OK", command=self.ok)
        button_ok.pack(side=LEFT, padx=10, pady=5, fill=BOTH, expand=True)
        button_cancel = Button(top, text="Zrušit", command=self.cancel)
        button_cancel.pack(side=LEFT, padx=10, pady=5, fill=BOTH, expand=True)

    def ok(self, event=None):
        self.ship.speed = int(self.spinbox_ship.get())
        self.top.destroy()

    def cancel(self, event=None):
        self.top.destroy()


class SetName:
    def __init__(self, parent, app):
        self.app = app
        top = self.top = Toplevel(parent)
        name = StringVar()
        name.set(app.name)

        top.title("Name")
        top.transient(parent)
        top.grab_set()
        top.focus_set()

        x = parent.winfo_x()
        y = parent.winfo_y()
        top.geometry("%dx%d+%d+%d" % (200, 100, x+200, y+100))

        container1 = Frame(top, width=400, pady=10, padx=10)

        label_name = Label(container1, text="Player name:")
        label_name.pack()

        self.entry_name = Entry(container1, textvariable=name)
        self.entry_name.pack()
        self.entry_name.focus_set()

        container1.pack(fill=BOTH)

        button_ok = Button(top, text="OK", command=self.ok)
        button_ok.pack(side=LEFT, padx=10, pady=5, fill=BOTH, expand=True)

    def ok(self, event=None):
        self.app.name = self.entry_name.get()
        self.top.destroy()
