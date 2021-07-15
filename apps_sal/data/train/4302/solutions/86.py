def better_than_average(class_points, your_points):
    sum = 0 
    for i in class_points: 
        sum = sum + i 
    avg = (sum+your_points)/(len(class_points)+1)
    return your_points > avg
