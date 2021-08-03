t = int(input())
for x in range(t):
    n = int(input())
    n *= 2
    a = int(n ** 0.5)
    if a * (a + 1) <= n:
        print(a)
    else:
        print(a - 1)
