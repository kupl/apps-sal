def find_multiples(integer, limit):
    lst = []
    acc = integer
    for num in range(integer, limit + 1):
        if acc <= limit:
            lst.append(acc)
            acc += integer
    return lst
