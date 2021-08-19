t = int(input())
for i in range(t):
    (a, k) = list(map(int, input().split()))
    (x1, x2, x3) = list(map(int, input().split()))
    big = max(x1, x2, x3)
    small = min(x1, x2, x3)
    q = big - small - 2 * k
    if q >= a:
        print(0)
    elif -1 * q >= 0:
        print(a * a)
    else:
        print(a * (a - q))
