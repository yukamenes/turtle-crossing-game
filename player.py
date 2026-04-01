"""
Module representing the player.

Handles:
- Player movement
- Detecting when the player reaches the finish line
- Detecting collisions with cars
"""

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """
    Represents the player character (turtle).

    Handles movement and interaction with game elements.
    """
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.up()
        self.goto(STARTING_POSITION)
        self.seth(90)
        
    def move(self):
        """
        Moves the player forward by a fixed distance.
        """
        self.fd(MOVE_DISTANCE)
    
    def check_end_of_screen(self):
        """
        Checks if the player reached the finish line.

        Returns:
            bool: True if the player reached the top, otherwise False.
        """
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        return False
    
    def check_collision(self, obstacle):
        """
        Checks if the player collided with a given obstacle.

        Args:
            obstacle (Turtle): The object to check collision with.

        Returns:
            bool: True if collision occurred, otherwise False.
        """
        if self.distance(obstacle) < 20:
            return True
        return False



