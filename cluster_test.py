from point import Point
from moving_test_point import MovingTestPoint
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.colors as col
import matplotlib.cm as cm

import platform
import matplotlib
if platform.system() == 'Darwin':
    matplotlib.use('MacOSX')

simulation_length = 2500
num_pts = 12
num_moving_pts = 1

num_colors = 500
color_nums = np.linspace(0x0000FF, 0xFF0000, num_colors)
colors = [f"{'#' + '0' * (6 - len(hex(int(color))[2:])) + hex(int(color))[2:]}" for color in color_nums]
print(colors)
cmap_colors = col.ListedColormap(colors, 'indexed')
cm.register_cmap(cmap=cmap_colors)

    
def __main__():

    pnts = []
    mvng_pnts = []
    color_indicies = []

    points = {
        'x': [],
        'y': [],
        'z': [],
    }

    x_dot = 0
    y_dot = 0
    z_dot = 0

    damping = 1.0

    for i in range(num_pts):
        pnt = Point(np.random.uniform(10000000000, 20000000000),
                          np.random.uniform(-10000000, 10000000),
                          np.random.uniform(-10000000, 10000000),
                          np.random.uniform(-10000000, 10000000),
                          0.1)
        pnts.append(pnt)
        
    
        print(f"Point {i + 1} Mass: {pnt.mass},\n"
              f"Point {i + 1} X: {pnt.x},\n"
              f"Point {i + 1} Y: {pnt.y},\n"
              f"Point {i + 1} Z: {pnt.z},\n"
              f"movable={pnt.movable}\n")

    for i in range(num_moving_pts):
        pnt = Point(np.random.uniform(10, 20),
                          np.random.uniform(-10000000, 10000000),
                          np.random.uniform(-10000000, 10000000),
                          np.random.uniform(-10000000, 10000000),
                          0.1)
        pnt.__class__ = MovingTestPoint
        pnt.movable = True
        mvng_pnts.append(pnt)

        print(f"Point {i + 1} Mass: {pnt.mass},\n"
              f"Point {i + 1} X: {pnt.x},\n"
              f"Point {i + 1} Y: {pnt.y},\n"
              f"Point {i + 1} Z: {pnt.z},\n"
              f"movable={pnt.movable}\n")

    for i in range(simulation_length):
        for mv_pnt in mvng_pnts:
            all_pnts = pnts + mvng_pnts
            
            for p in all_pnts:
                mv_pnt.move_because_of_object(p)

            points['x'].append(mv_pnt.x)
            points['y'].append(mv_pnt.y)
            points['z'].append(mv_pnt.z)

            saturated_value = 0
            max = 80000.0
            velocity = mv_pnt.get_velocity()
            if abs(velocity) > max:
                saturated_value = len(colors)
            else:
                saturated_value = np.round(np.interp(velocity, [0, max], [0, len(colors)]))
            
            color_indicies.append(saturated_value)

    print(f"Length of points[\'x\']: {len(points['x'])}.")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # print(f"\n\n{points['x']},\n\n {points['y']},\n\n {points['z']}\n\n")

    ax.scatter(points['x'], points['y'],points['z'], c=color_indicies, cmap=cmap_colors, marker='.')

    points = {
        'x': [],
        'y': [],
        'z': [],
    }
    
    for pnt in pnts:
        points['x'].append(pnt.x)
        points['y'].append(pnt.y)
        points['z'].append(pnt.z)

    ax.scatter(points['x'], points['y'],points['z'], c='b', marker='o')

    plt.show()

if __name__ == '__main__':
    __main__()