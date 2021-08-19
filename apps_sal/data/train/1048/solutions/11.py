t = int(input())


def shift(a, b, k):
    if k == 0:
        return a
    if k > abs(a - b):
        return b
    else:
        return a + (b - a) / abs(b - a) * k


while t > 0:
    (a, k) = map(int, input().split())
    vals = map(int, input().split())
    (x1, x2, x3) = sorted(vals)
    mid = (x1 + x3) / 2
    if x2 - x1 < a or x3 - x2 < a:
        overlapping = True
    x2 = shift(x2, mid, k)
    x1 = shift(x1, x2, k)
    x3 = shift(x3, x2, k)
    overlap = (a - (x3 - x1)) * a
    if overlap < 0:
        print(0)
    else:
        print(overlap)
    t -= 1
