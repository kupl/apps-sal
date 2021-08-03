def better_than_average(class_points, your_points):
    total = 0
    for point in class_points:
        total += point

    average = total / len(class_points)

    if your_points >= average:
        return True
    else:
        return False
