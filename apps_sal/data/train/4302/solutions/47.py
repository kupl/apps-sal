def better_than_average(class_points, your_points):
    return ((sum(class_points) + your_points) // (len(class_points) + 1)) <= your_points
