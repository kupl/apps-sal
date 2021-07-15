def better_than_average(class_points, your_points):
    total = 0
    for element in class_points:
        total += element
    class_average = total / len(class_points)
    if your_points > class_average:
        return True
    else:
        return False
