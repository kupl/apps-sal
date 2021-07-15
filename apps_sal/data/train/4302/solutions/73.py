def better_than_average(class_points, my_points):
    return my_points > sum(class_points)/len(class_points)
