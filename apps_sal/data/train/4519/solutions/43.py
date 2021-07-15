def max_number(n):
    l = [str(i) for i in str(n)]
    l.sort(reverse=True)
    k = int("".join(l))
    return k
