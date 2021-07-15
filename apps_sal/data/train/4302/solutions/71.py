import statistics as stat
def better_than_average(class_points, your_points):
    return stat.mean(class_points) < your_points

