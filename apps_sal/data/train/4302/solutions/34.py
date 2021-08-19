def better_than_average(class_points, your_points):
    average = 0
    for point in class_points:
        average += point
    if your_points > average / len(class_points):
        return True
    else:
        return False
