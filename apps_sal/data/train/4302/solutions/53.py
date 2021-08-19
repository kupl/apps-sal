def better_than_average(class_points, your_points):
    x = sum(class_points) + your_points
    average = x / (len(class_points) + 1)
    if average < your_points:
        return True
    else:
        return False
