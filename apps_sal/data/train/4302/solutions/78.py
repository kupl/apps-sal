def better_than_average(class_points, your_points):
    neu = 0
    for i in range(0,len(class_points)):
        b = class_points[i]
        neu += class_points[i]
    a = (neu + your_points) / (len(class_points) + 1)
    if your_points > a:
        return True
    else:
        return False

