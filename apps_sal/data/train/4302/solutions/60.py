def better_than_average(class_points, your_points):
    # Your code here
    result = sum(class_points) / len(class_points)
    if float(result) <= your_points:
        return True
    else:
        return False
