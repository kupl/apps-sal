# cook your dish here
n, m = map(int, input().split())
for i in range(m):
    x = int(input())
    a = 0
    if (n + 2) > x or x > (3 * n):
        a = 0
    elif (2 * n) + 1 == x:
        a = n
    elif (2 * n) + 1 > x:

        a = n - (((2 * n) + 1) - x)
    else:
        a = n - (x - ((2 * n) + 1))
    print(a)
