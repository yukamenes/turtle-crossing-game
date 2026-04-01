"""
Module for displaying and updating the game score.

Handles:
- Displaying current level
- Showing game over message
"""

from turtle import *

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Displays the player's progress (level) and game over message.
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        self.up()
        self.goto(-280, 250)
        self.update_score()

    def update_score(self):
        """
        Clears the previous score and writes the updated level.
        """
        self.clear()
        self.write(f"Level: {self.score}", font = FONT)

    def game_over(self):
        """
        Displays the 'GAME OVER' message in the center of the screen.
        """
        self.goto(-85,0)
        self.write("GAME OVER", font = FONT)


