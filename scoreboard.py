from turtle import Turtle
import time
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.level_update()


    def level_update(self):
        self.clear()
        self.write(f'Level {self.level}', align='center', font=FONT)

    def level_increase(self):
        self.level += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=('Arial', 20, 'normal'))
        time.sleep(1)
        self.goto(0, 260)
