def squares_needed(grains):
    count = 0
    total = 1
    while total <= grains:
        a = total * 2
        total = a
        count += 1
    return count

