def fold_to(distance):
    thickness = 0.0001
    if distance < 0:
        return None
    else:
        i = 0
        while thickness < distance:
            thickness = thickness * 2
            i = i + 1
        return i
