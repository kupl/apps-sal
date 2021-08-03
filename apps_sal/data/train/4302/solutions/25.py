def better_than_average(class_points, your_points):
    avg = 0
    total = 0
    for x in range(0, len(class_points)):
        total += class_points[x]
    avg = total / len(class_points)
    if avg > your_points:
        return False
    return True
