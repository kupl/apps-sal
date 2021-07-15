def fold_to(distance):
    if distance < 0:
        return None
    thickness = 0.0001
    idx = 0
    while thickness < distance:
        thickness *= 2
        idx +=1 
    return idx
