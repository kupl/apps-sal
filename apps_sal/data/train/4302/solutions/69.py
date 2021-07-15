def better_than_average(class_points, your_points):
    s = sum(class_points)
    u = len(class_points)
    m = s/u
    if m < your_points:
        return True
    else:
        return False
