def find_multiples(integer, limit):
    list = []
    for x in range(integer, limit + 1):
        if not x % integer:
            list.append(x)
    return list
