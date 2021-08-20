for _ in range(int(input())):
    (f, b, l, r, t, d) = input().split()
    ans = False
    if (f == l or f == r) and (f == t or f == d):
        ans = True
    if (b == l or b == r) and (b == t or b == d):
        ans = True
    if (t == l or t == r) and (t == f or t == b):
        ans = True
    if (d == l or d == r) and (d == f or d == b):
        ans = True
    if (l == f or l == b) and (l == t or l == d):
        ans = True
    if (r == f or r == b) and (r == t or r == d):
        ans = True
    print('YES' if ans else 'NO')
