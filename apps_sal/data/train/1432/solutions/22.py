def f(n, c):
    if c <= n:
        return 0
    if c == n * n:
        return n - 1
    e = n - 1
    s = n
    while c > s:
        s += 2 * e
        e -= 1
    return n - 1 - e


t = int(input())
for it in range(t):
    n = int(input())
    c = 0
    for i in range(n):
        a = input().split()
        c += a.count('1')
    print(f(n, c))
