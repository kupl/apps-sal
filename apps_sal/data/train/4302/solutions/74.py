def better_than_average(class_points, your_points):
    sum = your_points
    for elements in class_points:
        sum += elements
    average = sum / (len(class_points) + 1)
    if your_points > average:
        return True
    return False
