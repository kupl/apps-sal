t = int(input())
for _ in range(t):
    a = 0
    n = int(input())
    while n > 0:
        a += n * n
        n -= 2
    print(a)
