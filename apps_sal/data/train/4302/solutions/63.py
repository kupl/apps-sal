def better_than_average(class_points, your_points):
    x = 0
    for i in range(len(class_points)):
        x = x + class_points[i]
    y = x / len(class_points)
    if your_points > y:
        return True
    else:
        return False
