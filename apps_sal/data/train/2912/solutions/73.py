def find_multiples(integer, limit):
    l = []
    i = integer
    while integer <= limit:
        l.append(integer)
        integer += i

    return l
