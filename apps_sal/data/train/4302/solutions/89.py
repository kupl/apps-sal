def better_than_average(class_points, your_points):
    n = len(class_points)
    ave = (sum(class_points) + your_points) // n
    if your_points >= ave:
        return bool(your_points >= ave)
    else:
        return bool(your_points >= ave)
