import time

import tkinter as tk

from environment import *


world_size_x = 200
world_size_y = 200


# Initialize world
max_speed = 20
env = Environment(x_len=world_size_x, y_len=world_size_y, max_speed=max_speed)

# Add a Ball item to world
ball1 = Ball('Ball1', x_len=world_size_x, y_len=world_size_y)
ball2 = Ball('Ball2', x_len=world_size_x, y_len=world_size_y)
env.add_environment_item(ball1)
env.add_environment_item(ball2)

# Render world at 30fps
env.render()