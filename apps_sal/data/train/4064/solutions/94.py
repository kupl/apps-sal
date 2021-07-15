def count_by(x, n):
    counter = 1
    s = 0
    lst = []
    while counter <= n:
        s += x
        lst.append(s)
        counter += 1
    return lst
