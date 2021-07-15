# It's nice to put the OEIS but it's not that interesting if they give the algo
def is_keith_number(n):
    if n < 10: return False
    x = list(map(int, str(n)))
    y, i = sum(x), 1
    while y < n:
        i, x, y = i+1, x[1:]+[y], 2*y-x[0]
    return i * (y==n)
