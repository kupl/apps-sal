t = int(input())
for i in range(t):
    (a, k) = list(map(int, input().split()))
    (x1, x2, x3) = list(map(int, input().split()))
    big = max(x1, x2, x3)
    small = min(x1, x2, x3)
    if big - small - 2 * k >= a:
        print(0)
    elif small - big + 2 * k >= 0:
        print(a * a)
    else:
        print(a * (a - (big - small - 2 * k)))
