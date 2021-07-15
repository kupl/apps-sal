def find_multiples(integer, limit):
    return [integer * mult for mult in range(1, limit // integer + 1)]
