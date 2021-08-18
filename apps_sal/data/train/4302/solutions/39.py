def better_than_average(class_points, your_points):
    x = len(class_points)
    z = 0
    for k in class_points:
        z += k
    if your_points > z / x:
        return True
    else:
        return False
