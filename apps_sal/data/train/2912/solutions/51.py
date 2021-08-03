def find_multiples(integer, limit):
    m = 1
    new_list = []
    new_integer = integer
    while new_integer < limit:
        new_integer = integer * m
        if new_integer > limit:
            break
        new_list.append(new_integer)
        m += 1
    return new_list
