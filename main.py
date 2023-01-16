import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()


scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, 'Up')
car_manager = CarManager()
car_2 = CarManager()






game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    if player.ycor() > 260:
        scoreboard.level_increase()
        scoreboard.level_update()
        car_manager.move_increment()
        player.restart_position()
    for car in car_manager.cars:
        if player.distance(car) < 20:

            scoreboard.game_over()
            scoreboard.level = 1
            scoreboard.level_update()
            car_manager.move_distance = 5
            player.restart_position()














