t = int(input())
for i in range(t):
    a, k = list(map(int, input().split()))
    x1, x2, x3 = list(map(int, input().split()))
    big = max(x1, x2, x3)
    small = min(x1, x2, x3)
    if small - big + 2 * k >= 0:
        print(a * a)
    else:
        q = a - (big - small - 2 * k)
        if q == 0 or q < 0:
            print(0)
        else:
            print((q) * a)
