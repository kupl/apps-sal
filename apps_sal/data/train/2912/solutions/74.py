def find_multiples(integer, limit):
    list = []
    i = 1
    m = integer
    for m in range(integer, limit + 1):
        if (m >= integer) and (m == integer * i) and (m <= limit):
            list.extend([m])
            i = i + 1
            m = m * i
    return list
