def multiples(m, n):
    lst = []
    st = 1
    while len(lst) < m:
        a = n * st
        lst.append(a)
        st += 1
    return lst
