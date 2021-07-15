def better_than_average(class_points, your_points):
    classA = sum(class_points) / len(class_points)
    return True if your_points >= classA else False
