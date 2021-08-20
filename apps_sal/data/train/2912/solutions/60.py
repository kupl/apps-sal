def find_multiples(integer, limit):
    lst = []
    for item in range(integer, limit + 1, 1):
        if item % integer == 0:
            lst.append(item)
    return lst
