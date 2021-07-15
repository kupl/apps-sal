def fold_to(distance):
    if distance <0 : return None
    d = 0.0001
    n = 0
    while(d<distance) : 
        d *=2
        n +=1
    return n
