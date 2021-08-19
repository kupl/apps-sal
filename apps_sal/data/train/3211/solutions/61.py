def divide(weight):
    possible = [x for x in range(2, weight, 2) if (weight - x) % 2 == 0]
    return len(possible) > 0
