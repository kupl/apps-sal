def better_than_average(class_points, your_points):
    class_avg = sum(class_points) // len(class_points)
    return True if class_avg < your_points else False
