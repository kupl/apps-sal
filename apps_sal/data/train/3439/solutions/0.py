def solve(n):
    if n < 10:
        return n
    a = int((len(str(n)) - 1) * '9')
    b = n - a
    return sum([int(i) for i in list(str(a)) + list(str(b))])
