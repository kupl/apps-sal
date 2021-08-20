def fold_to(distance):
    thickness = 0.0001
    i = 0
    if distance > 0:
        while distance > thickness:
            thickness *= 2
            i += 1
        return i
    elif distance == 0:
        return 0
    else:
        return None
