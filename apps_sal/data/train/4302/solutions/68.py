def better_than_average(class_points, your_points):
    class_average = (sum(class_points) / len(class_points))
    print(class_average)
    your_average = [your_points]
    if your_average[0] > class_average:
        return True
    else:
        return False
