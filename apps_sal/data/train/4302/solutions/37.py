def better_than_average(class_points, your_points):
    num = 0
    for i in class_points:
        num += i
    length = len(class_points)
    divide = num / length
    if divide < your_points:
        return True
    elif divide > your_points:
        return False
