def fold_to(distance):
    thicc = 0.0001
    counter = 0
    if distance >= 0:
        while thicc < distance:
            thicc = thicc * 2
            counter += 1
    else:
        counter = None
    return counter
