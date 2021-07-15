def better_than_average(class_points, your_points):
    result = (sum(class_points) + your_points) / (len(class_points) + 1)
    if result < your_points:
        return True
    else:
        return False
