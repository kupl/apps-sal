def solve(n):
    a,b = '01'
    for _ in range(n): a,b = a+b,a
    return a
