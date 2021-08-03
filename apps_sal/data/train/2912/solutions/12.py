def find_multiples(integer, limit):
    return [integer * count for count in range(1, int(limit / integer) + 1)]
