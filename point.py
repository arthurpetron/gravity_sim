import numpy as np


class Point:

    def __init__(self, mass: float, x: float, y: float, z: float, dt: float, movable = False):

        self.mass = mass
        self.x = x
        self.y = y
        self.z = z
        self.movable = movable

        self.dt = dt
        self.velocity_x = 0.0
        self.velocity_y = 0.0
        self.velocity_z = 0.0
        self.acceleration_x = 0.0
        self.acceleration_y = 0.0
        self.acceleration_z = 0.0

    def get_velocity(self):
        mag_vel = np.sqrt(np.power(self.velocity_x, 2) + np.power(self.velocity_y, 2) + np.power(self.velocity_z, 2))
        return mag_vel
