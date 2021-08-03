def better_than_average(class_points, your_points):
    if (float(sum(class_points)) / max(len(class_points), 1)) < your_points:
        return True
    return False
