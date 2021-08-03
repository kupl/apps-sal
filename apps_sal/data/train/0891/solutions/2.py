n, m = map(int, input().split())
for i in range(m):
    x = int(input())
    if (n + 2) > x or x > (3 * n):
        print(0)
    elif (2 * n) + 1 == x:
        print(n)
    elif (2 * n) + 1 > x:
        print(n - (((2 * n) + 1) - x))
    else:
        print(n - (x - ((2 * n) + 1)))
