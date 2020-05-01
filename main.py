from meters.meters_100 import *
from meters.meters_400 import *
from meters.meters_1500 import *


class InitiateGameFrame(Frame):
    def __init__(self, master, name):
        Frame.__init__(self, master)
        self.grid()
        self.name = name
        self.master = master
        Label(self, text='Which game would you like to play, ' + name + '?')
        Button(self, text='>>Play decathlon 100!<<', command=self.initiate_game1).grid(
            row=1, column=0
        )
        Button(self, text='>>Play decathlon 400!<<', command=self.initiate_game2).grid(
            row=2, column=0
        )
        Button(self, text='>>Play decathlon 1500!<<', command=self.initiate_game3).grid(
            row=3, column=0
        )

    def initiate_game1(self):
        self.destroy()
        Decathlon100Meters(self.master, self.name)

    def initiate_game2(self):
        self.destroy()
        Decathlon400Meters(self.master, self.name)

    def initiate_game3(self):
        self.destroy()
        Decathlon1500Meters(self.master, self.name)


player_name = input('Please enter you name: ')
root = Tk()
root.title('meters')
game = InitiateGameFrame(root, player_name)
game.mainloop()
