import statistics 
def better_than_average(class_points, your_points):
    return statistics.mean(class_points) < your_points
