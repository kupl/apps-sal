def better_than_average(class_points, your_points):
    class_total = sum(class_points)
    class_avg = class_total/len(class_points)
    
    return your_points > class_avg
