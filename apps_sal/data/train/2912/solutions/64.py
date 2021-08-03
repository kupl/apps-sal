def find_multiples(integer, limit):
    list = []
    i = integer
    for i in range(limit + 1):
        if i % integer == 0 and i != 0:
            list.append(i)
    return list
