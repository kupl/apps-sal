def fold_to(distance):
    count = 0
    p_thickness = 0.0001
    if distance >= 0:
        while p_thickness < distance:
            p_thickness *=2
            count += 1
        return count
    else:
        return None
