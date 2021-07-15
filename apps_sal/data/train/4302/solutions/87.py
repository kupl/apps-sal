def better_than_average(class_points, your_points):
    total_points = your_points
    for points in class_points:
        total_points += points
    avg_points = int(total_points/(len(class_points)+1))
    return your_points >= avg_points
