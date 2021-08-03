def better_than_average(class_points, your_points):
    sum = your_points
    for number in class_points:
        sum += number
    average = sum / (len(class_points) + 1)
    if your_points > average:
        return True
    else:
        return False

    # Your code here
