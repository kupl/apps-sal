def solve(n):
    x, y = '0', '01'
    for i in range(n):
        x, y = y, y+x
    return x
