def better_than_average(class_points, your_points):
    totalScore = 0
    
    for points in class_points:
        totalScore += points
    
    average = totalScore / len(class_points)
    
    return your_points > average
