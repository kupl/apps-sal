def square_up(n):
    lst = []
    max = 1
    while max <= n:
        for x in range(n, 0, -1):
            if x - max < 1:
                lst.append(x)
            else:
                lst.append(0)
        max += 1

    return lst
