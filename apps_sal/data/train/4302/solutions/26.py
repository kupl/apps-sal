def better_than_average(class_points, your_points):
    average = (sum(class_points) / len(class_points))
    if average < your_points:
        Better = True
    else:
        Better = False
    return Better
