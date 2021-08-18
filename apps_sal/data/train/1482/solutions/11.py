t = int(input())
for i in range(t):
    n = int(input())
    q = 10**(n - int((n + 1) / 2))
    p = 1
    if n == 1:
        q = 1
    print(p, q)
