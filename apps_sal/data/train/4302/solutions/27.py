def better_than_average(class_points, your_points):
    from statistics import mean
    if mean(class_points) >= your_points:
        return False
    else:
        return True
