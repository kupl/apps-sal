def fold_to(distance):
    paper=0.0001
    i=0
    if distance<0:return None
    while paper<distance:
        i+=1
        paper*=2
    return i
