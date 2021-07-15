def fold_to(distance):
    thick=0.0001
    i=0
    if distance<0:
        return None
    else:
        while thick<distance:
            thick=2*thick;
            i=i+1;
    return i
    #your code here

