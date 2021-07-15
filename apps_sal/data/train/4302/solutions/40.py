def better_than_average(class_points, your_points):
    points = 0
    for point in class_points:
        points += point
    return your_points > points/len(class_points)
