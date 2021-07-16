import numpy as np
from point import Point

velocity_damping = 0.000000
gravitational_constant = -1000000.0


class MovingTestPoint(Point):
    
    def move_because_of_object(self, _point_object):

        if not self.movable:
            return

        if _point_object.__hash__() == self.__hash__():
            return
        
        pt_dx = self.x - _point_object.x
        pt_dy = self.y - _point_object.y
        pt_dz = self.z - _point_object.z

        d = np.sqrt(np.power(pt_dx, 2) + np.power(pt_dy, 2) + np.power(pt_dz, 2))

        if d == 0:
            return 0

        force = gravitational_constant * self.mass * _point_object.mass / np.power(d / 2.0, 2)

        fx = force * pt_dx / d
        fy = force * pt_dy / d
        fz = force * pt_dz / d 

        self.acceleration_x = fx / self.mass * -np.sign(fx / pt_dx)
        self.acceleration_y = fy / self.mass * -np.sign(fy / pt_dy)
        self.acceleration_z = fz / self.mass * -np.sign(fz / pt_dz)

        self.velocity_x += self.acceleration_x * self.dt / 2.0
        self.velocity_y += self.acceleration_y * self.dt / 2.0
        self.velocity_z += self.acceleration_z * self.dt / 2.0

        self.velocity_x *= (1 - self.velocity_x * velocity_damping)

        dx = self.velocity_x * self.dt
        dy = self.velocity_y * self.dt
        dz = self.velocity_z * self.dt

        self.x += dx
        self.y += dy
        self.z += dz

