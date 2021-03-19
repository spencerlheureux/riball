import math
import time
from random import randint

import tkinter as tk


# TODO: Genericize Environment class more, create an inherited class 
# that is more specific to my example use case


class Environment(object):
    """ Environment

    Represents a simple world, and all information about its state.

    """

    def __init__(self, x_len=500, y_len=500, max_speed=20):
        self.x_len = x_len
        self.y_len = y_len
        self.items = {}
        self.max_speed = max_speed
        self.time_step = 1/max_speed

    def add_environment_item(self, item):
        """ Add an EnvironmentItem to the Environment"""
        # TODO: Add logic to check if item is valid for this world
        self.items[item.name] = item

    def take_action(self, action):
        # TODO: Genericize action taking, maybe include object name
        # in action to specify an action to take on a specific item 
        self.items['name'].take_action(action)

    def increment_time(self):
        # TODO: Somehow allow for object interactions
        # TODO: Create a built-in rewards system with generic architecture
        for item in self.items.values():
            item.increment_time(self.time_step)
        self.interactions()
    
    def interactions(self):
        # TODO: Look into making this cleaner? More efficient?
        for name, item in self.items.items():
            for secondary_item in self.items.values():
                if name != secondary_item.name:
                    item.interaction(secondary_item)

    def get_world_state(self):
        return [attr for item in self.items.values() 
                for attr in item.get_state()]

    def render(self):
        """ Render world """
        window = tk.Tk()
        frame = tk.Frame(master=window, width=self.x_len, height=self.y_len)
        frame.pack()
        labels = [(item, tk.Label(master=frame, text=f"{item.name}", bg="red")) 
                  for item in self.items.values()]

        # Run world
        frame_number = 0
        while True:
            for item, label in labels:
                label.place(x=item.x_pos, y=item.y_pos)
            self.increment_time()
            if frame_number >= self.max_speed:
                frame.update()
                time.sleep(0.033)
                frame_number = 0
            else:
                frame_number += 1


class EnvironmentItem(object):
    """ EnvironmentItem

    Higher-level template class for any items in environment
    """
    def __init__(self, name, *args, **kwargs):
        self.state_variables = ['x_pos', 'y_pos', 'x_vel', 'y_vel']
        self.set_initial_state(kwargs)
        self.name = name

    def set_initial_state(self, kwargs):
        for var in self.state_variables:
            if var in kwargs:
                setattr(self, var, kwargs[var])
            else:
                setattr(self, var, 0)
    
    def get_state(self):
        return [self.x_len, self.y_len, self.x_pos, 
                self.y_pos, self.x_vel, self.y_vel]

    def take_action(self, action):
        """ Custom action to be taken by object """

    def increment_time(self):
        """ Custom time increment for object """

    def interaction(self, obj):
        """ Custom definition for interactions with obj """


if __name__ == '__main__':
    # To test class states
    x_len = 500
    y_len = 500
    world = Environment(x_len=x_len, y_len=y_len)
