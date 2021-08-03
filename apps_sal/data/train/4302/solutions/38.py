def better_than_average(class_points, your_points):
    s = 0
    avg = 0
    for i in class_points:
        s += i
    avg = s / len(class_points)
    print(avg)
    if avg < your_points:
        return True
    else:
        return False
