def find_multiples(integer, limit):
    return [integer * i for i in range(1, limit // integer + 1)]
