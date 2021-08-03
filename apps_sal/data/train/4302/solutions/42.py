def better_than_average(class_points, your_points):
    return False if sum(class_points) // len(class_points) >= your_points else True
