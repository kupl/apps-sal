def distribute(m, n):
    lst = []
    if n > 0:
        lst = [0 for i in range(n)]
        if m > 0:
            for j in range(m):
                lst[j % n] += 1
    return lst
