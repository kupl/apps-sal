def better_than_average(class_points, your_points):
    mean_class_points = sum(class_points) / len(class_points)
    if mean_class_points >= your_points:
        return False
    if mean_class_points <= your_points:
        return True
