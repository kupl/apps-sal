def better_than_average(class_points, your_points):
    a = sum(class_points) + your_points
    res = a / (len(class_points) + 1)
    if your_points > res:
        return True
    else:
        return False
