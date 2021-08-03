t = int(input())
for i in range(t):
    n = int(input())
    r = int(n**(.5))
    d = n - r * r
    m = d % r
    print('X' * m + 'D' * (m > 0) + 'X' * (r - m) + 'D' * (r + d // r))
