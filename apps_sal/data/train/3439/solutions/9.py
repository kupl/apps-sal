def solve(n):
    n = str(n)
    a = str(int(n[0]) - 1) + '9' * (len(n) - 1)
    b = str(int(n) - int(a))
    return sum(int(i) for i in a + b) if int(n) else 0
