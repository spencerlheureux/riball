import math
from random import randint

from environment import EnvironmentItem


class Ball(EnvironmentItem):
    """ Ball

    Represents a ball moving through the world.
    """
    def __init__(self, *args, x_len=500, y_len=500, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_len = x_len
        self.y_len = y_len
        self.x_pos = randint(1, x_len)
        self.y_pos = randint(1, y_len)
        self.x_vel = randint(1, 4)
        self.y_vel = randint(1, 4)
    
    def increment_time(self, time_step):
        if self.x_pos <= 0 or self.x_pos >= self.x_len:
            self.x_vel = -1 * self.x_vel
        if self.y_pos <= 0 or self.y_pos >= self.y_len:
            self.y_vel = -1 * self.y_vel
        self.x_pos += (self.x_vel * time_step)
        self.y_pos += (self.y_vel * time_step)

    def interaction(self, obj):
        # Sample interaction, if another ball gets too close, reset position
        distance = math.sqrt((self.x_pos - obj.x_pos)**2 + (self.y_pos - obj.y_pos)**2)
        if distance <= 50 and distance >= 49:
            self.x_pos = randint(1, self.x_len)
            self.y_pos = randint(1, self.y_len)


class Catcher(EnvironmentItem):
    """ Catcher

    Represents a catcher
    """