import pygame
import time


class Day_time:
    def __init__(self):
        # One second in game
        self.game_time_speed = 10

        # Game time
        self.game_hour = 18
        self.game_minute = 0

        # Start time for reset
        self.start_time = time.time()

    def reset_time_status(self):
        if self.game_minute >= 59:
            self.start_time = self.current_time
            self.game_hour += 1

        if self.game_hour >= 24:
            self.start_time = self.current_time
            self.game_hour = 0

    def update(self):
        # Current time for reset
        self.current_time = time.time()

        # Reset time
        self.reset_time_status()


        self.game_minute = int((self.current_time - self.start_time) * 10)

        self.return_time = str(self.game_hour) + ':' + str(self.game_minute)
        return self.return_time



