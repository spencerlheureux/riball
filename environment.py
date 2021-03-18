from random import randint


class Environment(object):
    """ Environment

    Represents a world/window.
    """

    def __init__(self, x_len=500, y_len=500):
        self.x_len = x_len
        self.y_len = y_len
        self.items = []

    def add_environment_item(self, item):
        """ Add an EnvironmentItem to the Environment"""
        # TODO: Add logic to check if item is valid for this world
        self.items.append(item)

    def take_action(self, action):
        self.catcher.take_action(action)

    def increment_time(self):
        # TODO: Somehow allow for object interactions
        for item in self.items:
            item.increment_time()

    def get_world_state(self):
        return [attr for item in self.items for attr in item.get_state()]


class EnvironmentItem(object):
    """ EnvironmentItem

    Higher-level template class for any items in environment
    """
    def __init__(self, *args, **kwargs):
        self.state_variables = ['x_pos', 'y_pos', 'x_vel', 'y_vel']
        self.set_initial_state(kwargs)
        self.name = None
        if 'name' in kwargs:
            self.name = kwargs['name']

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
        """ Custom action to be taken by object"""

    def increment_time(self):
        """ Custom time increment for object"""


class Ball(EnvironmentItem):
    """ Ball

    Represents a ball moving through the world.
    """
    def __init__(self, *args, x_len=500, y_len=500, **kwargs):
        super().__init__(*args, **kwargs)
        self.x_len = x_len
        self.y_len = y_len
        self.x_pos = randint(0, x_len)
        self.y_pos = randint(0, y_len)
        self.x_vel = randint(1, 4)
        self.y_vel = randint(1, 4)
    
    def increment_time(self):
        for x in range(abs(self.x_vel)):
            if self.x_vel > 0:
                self.x_pos += 1
            elif self.x_vel < 0:
                self.x_pos += -1
            if self.x_pos >= self.x_len or self.x_pos <= 0:
                self.x_vel = -1 * self.x_vel
        for y in range(abs(self.y_vel)):
            if self.y_vel > 0:
                self.y_pos += 1
            elif self.y_vel < 0:
                self.y_pos += -1
            if self.y_pos >= self.y_len or self.y_pos <=0 :
                self.y_vel *= -1


class Catcher(EnvironmentItem):
    """ Catcher

    Represents a catcher
    """


if __name__ == '__main__':
    # To test class states
    x_len = 500
    y_len = 500
    world = Environment(x_len=x_len, y_len=y_len)
    ball = Ball(x_len=x_len, y_len=y_len)
    world.add_environment_item(ball)
    print(ball.get_state())
    for x in range(10):
        world.increment_time()
        print(ball.get_state())
        print(world.get_world_state())


