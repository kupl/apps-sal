def fold_to(distance):
    if distance >= 0:
        times = 0
        size = 0.0001
        while size < distance:
            size *= 2
            times += 1
        return times
    else:
        return None
