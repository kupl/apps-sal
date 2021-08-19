t = int(input())
for i in range(t):
    (a, k) = [float(i) for i in input().split()]
    p = [float(i) for i in input().split()]
    p.sort()
    (x1, x2, x3) = p
    x = min(x1 + 2 * k, x3)
    area = (a - (x3 - x)) * a
    if area <= 0:
        print(0)
    else:
        print(area)
