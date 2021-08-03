def better_than_average(class_points: [], your_points):
    result = 0
    for i in class_points:
        result += i
    result = result / len(class_points)
    if your_points > result:
        return True
    return False
