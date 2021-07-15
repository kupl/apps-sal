def better_than_average(class_points, your_points):
    return bool(sum(class_points)/len(class_points) <= your_points)
