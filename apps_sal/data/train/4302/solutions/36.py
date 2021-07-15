def better_than_average(class_points, your_points):
    average = (sum(class_points) + your_points)/(len(class_points) + 1)
    if your_points > average:
        return True
    return False

