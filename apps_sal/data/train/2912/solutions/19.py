def find_multiples(integer, limit):
    return [x for x in range(integer, limit + 1) if x % integer == 0]
