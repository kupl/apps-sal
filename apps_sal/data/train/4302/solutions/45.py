def better_than_average(class_points, your_points):
    
    avrg = (sum(class_points) +your_points)/(len(class_points)+1)
    if  your_points>avrg:
        return True
    else:
        return False
