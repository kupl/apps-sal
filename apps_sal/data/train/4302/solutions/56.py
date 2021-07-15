def better_than_average(class_points, your_points):
    l=len(class_points)
    s=sum(class_points)
    a=s/l
    if(your_points>a):
        return True
    else:
        return False
