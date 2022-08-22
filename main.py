import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
 
#see if the users presses the up arrow or down arrow key 

car_manager.create_car(6)
num_loop = 0
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
player.reset_position()
while game_is_on:

    car_manager.move_car()
    screen.update()
    if (num_loop % 6 == 0):
        car_manager.create_car(3)
    time.sleep(0.1)
    #detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 30:
            game_is_on = False
            scoreboard.game_over()
    num_loop += 1
    #detect successful crossing
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_score()
    screen.update()


screen.exitonclick()    

    
    
