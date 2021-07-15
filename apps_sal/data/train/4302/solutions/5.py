def better_than_average(class_points, your_points):
    # Your code here 
    num_of_class = len(class_points)
    class_score = sum(class_points) / num_of_class
    if class_score < your_points:
        return True
    else:
        return False
