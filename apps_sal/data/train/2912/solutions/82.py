def find_multiples(integer, limit):
    lst = []
    for i in range(1, limit):
        if i % integer == 0:
            lst.append(i)
    if limit % integer == 0:
        lst.append(limit)
    return lst
