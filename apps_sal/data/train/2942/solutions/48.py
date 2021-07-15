def fold_to(distance):
    if distance >= 0:
        counter = 0
        t = 0.0001
        while t < distance:
            t *= 2
            counter += 1
        return counter
