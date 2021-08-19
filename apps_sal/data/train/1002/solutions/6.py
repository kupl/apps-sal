def check(a, pos, d):
    if pos == 0 or pos == len(a) - 1:
        return True
    for i in range(pos + 1, len(a)):
        if a[i] - a[i - 2] > d:
            return False
    return True


def check2(a, pos, d):
    for i in range(pos - 1, -1, -1):
        if a[i + 2] - a[i] > d:
            return False
    return True


T = int(input())
for _ in range(T):
    (n, d) = list(map(int, input().split()))
    a = [int(e) for e in input().split()]
    startVal = a[0]
    a.sort()
    band = True
    startPos = 0
    for (i, e) in enumerate(a[1:]):
        if e - a[i] > d:
            band = False
            break
        if e == startVal:
            startPos = i + 1
    if band and (check(a, startPos, d) or check2(a, startPos, d)):
        print('YES')
    else:
        print('NO')
