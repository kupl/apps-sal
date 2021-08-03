n = int(input())
c = [list(map(int, input().split())) for _ in range(n)]
a, b = 0, 0
d = []
for i in range(n):
    if len(c[i]) % 2:
        a += sum(c[i][1:c[i][0] // 2 + 1])
        b += sum(c[i][c[i][0] // 2 + 1:])
    else:
        a += sum(c[i][1:c[i][0] // 2 + 1])
        b += sum(c[i][c[i][0] // 2 + 2:])
        d.append(c[i][c[i][0] // 2 + 1])
d.sort(reverse=True)
print(a + sum(d[0::2]), b + sum(d[1::2]))
