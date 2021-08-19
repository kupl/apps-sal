# cook your dish here
n, m = map(int, input().split())
for i in range(m):
    x = int(input())
    if x <= n or x > 3 * n:
        print(0)
    elif x > n and x <= 2 * n:
        print(x - n - 1)
    else:
        print(n - (x % (2 * n)) + 1)
