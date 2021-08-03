def sum_mul(n, m):

    lst = [x for x in range(n, m)]

    a = 1
    new = []
    for i in range(len(lst)):
        new.append(n * a)
        a += 1

    final = []
    for i in new:
        if i < m:
            final.append(i)

    if n <= 0 or m <= 0:
        return "INVALID"
    else:
        return sum(final)
