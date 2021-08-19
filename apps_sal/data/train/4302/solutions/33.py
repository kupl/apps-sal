def better_than_average(class_points, your_points):
    import numpy as np
    a = np.mean(class_points)
    if a < your_points:
        return True
    else:
        return False
