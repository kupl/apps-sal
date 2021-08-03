def better_than_average(class_points, your_points):
    total = sum(class_points)
    ave = total / len(class_points)
    if your_points > ave:
        return True
    else:
        return False
