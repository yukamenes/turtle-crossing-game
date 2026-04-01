"""
Main game loop module.

Responsible for:
- Setting up the screen
- Initializing game objects
- Handling user input
- Running the game loop
- Checking collisions and win/lose conditions
"""
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car_manager = CarManager()

player = Player()
scoreboard = Scoreboard()

screen.onkeypress(player.move, 'Up')

game_is_on = True
lose = False

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if not lose:
        car_manager.create_car()
        car_manager.move_cars()

        if player.check_end_of_screen():
            scoreboard.score += 1
            scoreboard.update_score()
            car_manager.increase_speed()

        for car in car_manager.cars:
            if car.xcor() < -350:
                car_manager.reset_car(car)

            if player.check_collision(car):
                lose = True

    if lose:
        scoreboard.game_over()