def fold_to(distance):
    if distance >= 0:
        thicc = 0.0001
        count = 0
        while thicc < distance:
            thicc = thicc * 2
            count += 1
        return count
    else:
        return None
