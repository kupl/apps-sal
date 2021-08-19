def max_number(n):
    # your code here
    m = list(map(int, str(n)))
    m.sort(reverse=True)
    return int("".join(str(x) for x in m))
