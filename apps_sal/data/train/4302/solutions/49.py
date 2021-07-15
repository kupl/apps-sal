def better_than_average(class_points, your_points):
    length_of_class_points = len(class_points)
    sum_of_numbers = 0
    for i in range(0, len(class_points)):
        sum_of_numbers = sum_of_numbers + class_points[i]
    average_number = round(sum_of_numbers / length_of_class_points)
    if your_points > average_number:
        return True
    else:
        return False
