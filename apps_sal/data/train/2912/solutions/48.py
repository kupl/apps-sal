def find_multiples(integer, limit):
    return [i for i in range(integer, limit + 1) if i % integer == 0]
