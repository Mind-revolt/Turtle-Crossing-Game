from turtle import Turtle, Screen
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_X = 280


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_distance = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6 or random_chance == 3:
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_number = random.randint(-240, 240)
            new_car.goto(STARTING_X, random_number)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.move_distance)

    def move_increment(self):
        self.move_distance += MOVE_INCREMENT









