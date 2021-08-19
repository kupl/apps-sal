def better_than_average(class_points, your_points):
    cavg = sum(class_points) / len(class_points)
    if your_points > cavg:
        return True
    else:
        return False
