n, k = map(int, input().split())
l = [*map(int, input().split())]

s = sum(l)
res = []
if s % k == 0:
    s //= k
    curr = 0
    prev = 0

    for i, e in enumerate(l):
        curr += e
        if curr == s:
            res.append(str(i - prev + 1))
            prev = i + 1
            curr = 0
        if curr > s:
            res = []
            break

    if curr != 0: res = []

if len(res) != k:
    print('No')
else:
    print('Yes')
    print(' '.join(res))
