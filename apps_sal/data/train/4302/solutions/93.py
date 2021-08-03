def better_than_average(class_points, your_points):
    class_points.append(your_points)
    return your_points > sum(class_points) // len(class_points)
