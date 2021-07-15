def better_than_average(class_points, your_points):
    class_points.append(your_points)
    avr = sum(class_points)/(len(class_points) - 1)
    if avr <= your_points:
        return True
    else:
        return False
