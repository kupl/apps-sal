t = int(input())
while t:
    t = t - 1
    (n, x) = input().split()
    n = int(n)
    x = int(x)
    (d, l) = input().split()
    if d == 'L':
        p = x
    elif d == 'R':
        p = n - x + 1
    if p % 2 == 1:
        if l == 'H':
            lang = 'H'
        else:
            lang = 'E'
    elif p % 2 == 0:
        if l == 'H':
            lang = 'E'
        else:
            lang = 'H'
    print(p, lang)
