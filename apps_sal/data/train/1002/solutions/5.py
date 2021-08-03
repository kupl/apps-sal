def left(a, pos):
    if pos == 0 or pos == len(a) - 1:
        return True
    for i in range(pos + 1, len(a)):
        if a[i] - a[i - 2] > d:
            return False
    return True


def right(a, pos):
    for i in range(pos - 1, -1, -1):
        if a[i + 2] - a[i] > d:
            return False
    return True


for _ in range(int(input())):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    startVal = a[0]
    a.sort()
    f = 1
    startPos = 0

    for i, e in enumerate(a[1:]):
        if e - a[i] > d:
            f = 0
            break
        if e == startVal:
            startPos = i + 1

    if f and (left(a, startPos) or right(a, startPos)):
        print("YES")
    else:
        print("NO")
