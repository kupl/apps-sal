def better_than_average(class_points, your_points):
    mu = sum(class_points) / len(class_points)
    if your_points > mu:
        return True
    else:
        return False

