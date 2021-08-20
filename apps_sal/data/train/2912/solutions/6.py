def find_multiples(integer, limit):
    return [i for i in range(0, limit + 1, integer) if i != 0]
