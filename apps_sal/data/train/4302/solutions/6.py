def better_than_average(class_points, your_points):
    i = 0
    totalP = 0
    while i < len(class_points):
        totalP += class_points[i]
        i += 1
    totalP = totalP / len(class_points)
    if totalP > your_points:
        return False
    else:
        return True
