def better_than_average(class_points, your_points):
    sum = 0
    for i in class_points:
        sum += i
    sum += your_points
    avg = sum / (len(class_points) + 1)
    if your_points > avg:
        return True
    else:
        return False
