def better_than_average(class_points, your_point):
    return sum(class_points) / len(class_points) < your_point
