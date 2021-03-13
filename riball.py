import time

import tkinter as tk

from environment import *


world_size_x = 200
world_size_y = 200


# Initialize world
env = Environment(x_len=world_size_x, y_len=world_size_y)
ball = Ball(x_len=world_size_x, y_len=world_size_y)
env.add_environment_item(ball)

# Initialize visuals
window = tk.Tk()
frame = tk.Frame(master=window, width=world_size_x, height=world_size_y)
frame.pack()
label = tk.Label(master=frame, text="Ball", bg="red")

# Run world
while True:
    label.place(x=ball.x_pos, y=ball.y_pos)
    frame.update()
    env.increment_time()
    time.sleep(0.033)
