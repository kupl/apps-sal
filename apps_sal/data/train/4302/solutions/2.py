import statistics
def better_than_average(class_points, your_points):
    return your_points > statistics.mean(class_points)
