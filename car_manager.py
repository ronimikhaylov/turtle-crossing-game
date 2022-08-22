from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        # 20px high by 40px wide
        self.height = 20
        self.width = 40
        self.color = random.choice(COLORS)

    def create_car(self, num_cars):
        for _ in range(num_cars):
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)
    
    
    def move_car(self):
        for car in self.cars:
            car.forward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        
    
  
