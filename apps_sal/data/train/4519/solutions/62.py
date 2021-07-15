def max_number(n):
    n = list(map(int,str(n)))
    n.sort(reverse = True)
    n = "".join(map(str, n))
    return int(n)

