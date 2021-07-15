def better_than_average(class_points, your_points):
    n=len(class_points)
    #print("e={}" .format(n))
    ave=(sum(class_points)+your_points)//n
    #print('ave={}' .format(ave))
    if your_points>=ave:
        return bool(your_points>=ave)
        #break
    else:
        return bool(your_points>=ave)
