def better_than_average(class_points, your_points):
    class_points.append(your_points)
    average = sum(class_points) / len(class_points)
    return [False, True][your_points > average]
