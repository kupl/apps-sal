def max_number(n):
    m = list(map(int, str(n)))
    m.sort(reverse=True)
    return int("".join(str(x) for x in m))
