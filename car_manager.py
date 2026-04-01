"""
Module responsible for managing cars (obstacles) in the game.

It handles:
- Creating new cars
- Moving all cars
- Resetting cars when they leave the screen
- Increasing movement speed as the game progresses
"""

from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    """
    Manages all cars in the game.

    Attributes:
        cars (list): List of all active car objects.
        speed (int): Current movement speed of all cars.
    """
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Randomly creates a new car and adds it to the cars list.
        The probability of creation is controlled by randint.
        """
        if randint(1, 8) == 1:
            car = Turtle()
            car.color(choice(COLORS))
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.penup()
            car.goto(320, randint(-250, 280))
            self.cars.append(car)

    def move_cars(self):
        """
        Moves all cars forward based on the current speed.
        """
        for car in self.cars:
            car.forward(self.speed)

    def reset_car(self, car):
        """
        Resets a car to the starting position on the right side
        with a random vertical position.

        Args:
            car (Turtle): The car object to reset.
        """
        car.goto(320, randint(-250, 280))
    
    def increase_speed(self):
        """
        Increases the speed of all cars to make the game harder.
        """
        self.speed += MOVE_INCREMENT