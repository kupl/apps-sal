t = int(input())
for i in range(t):
    c = 0
    n = int(input())
    while n > 0:
        c = c + n * n
        n = n - 2
    print(c)
