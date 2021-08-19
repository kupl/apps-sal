def fish(shoal):
    size = 1
    while count_lesser_fish(shoal, size) >= 2 * size * (size + 1):
        size += 1
    return size


def count_lesser_fish(shoal, size):
    return sum((int(f) for f in shoal if int(f) <= size))
