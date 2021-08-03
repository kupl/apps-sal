def find_multiples(integer, limit):
    list = []
    for n in range(integer, limit + 1, 1):
        if n % integer == 0:
            list.append(n)

    return list
