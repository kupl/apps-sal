import statistics
def better_than_average(class_points, your_points):
    class_points.append(your_points)
    avg = statistics.mean(class_points)
    return True if avg < your_points else False

