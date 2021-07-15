def better_than_average(class_points, your_points):
    count = 0
    average = 0
    for i in class_points:
        count += i
    average = count / len(class_points)
    if your_points > average:
        return True
    return False
