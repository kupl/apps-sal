(n, m) = list(map(int, input().split()))
np1 = n + 1
mp1 = m + 1
for i in range(1, 1 + n // 2):
    for j in range(1, mp1):
        print('%d %d\n%d %d' % (i, j, np1 - i, mp1 - j))
if n & 1:
    i = 1 + n // 2
    for j in range(1, 1 + m // 2):
        print('%d %d\n%d %d' % (i, j, i, mp1 - j))
    if m & 1:
        print(i, 1 + m // 2)
