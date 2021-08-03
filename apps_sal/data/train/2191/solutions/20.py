input()
s = sorted(set(map(int, input().split())))
c = m = 0
d = []
for b in s:
    d += [c] * (b - c)
    c = b
for b in s[-1::-1]:
    if b < m + 2:
        break
    m = max(m, c % b, *(a % b for a in d[2 * b - 1::b]))
print(m)
