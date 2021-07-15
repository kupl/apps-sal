def better_than_average(class_points, your_points):
    x = sum(class_points) / len(class_points) + 1
    y = your_points
    return x < y
