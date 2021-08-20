import math
n = int(input())
a = list(map(int, input().split()))
segs = []
st = -1
for i in range(n):
    iso = False if i == 0 or i == n - 1 else a[i - 1] == a[i + 1] and a[i] != a[i - 1]
    if iso and st == -1:
        st = i
    elif not iso and st != -1:
        segs.append((st, i - 1))
        st = -1
ans = 0
for (l, r) in segs:
    span = r - l + 1
    ans = max(ans, span)
    for i in range(span // 2):
        a[l + i] = a[l - 1]
        a[r - i] = a[r + 1]
    if span % 2:
        j = l + span // 2
        a[j] = sorted([a[j - 1], a[j], a[j + 1]])[1]
print(math.ceil(ans / 2))
print(*a)
