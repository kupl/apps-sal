def fold_to(distance):
    if distance < 0:
        return None
    else:
        counter = 0
        i = 0.0001
        while i <= distance:
            i *= 2
            counter += 1
        return counter
