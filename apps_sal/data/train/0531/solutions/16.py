# cook your dish here
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
a = a + [(float('inf'), -1)]

c = 0
_w = a[0][0]
for i in range(1, len(a)):
    if a[i][0] - a[i][1] > _w:
        c += 1
        _w = a[i][0]
    elif a[i][0] + a[i][1] < a[i + 1][0]:
        c += 1
        _w = a[i][0] + a[i][1]
    else:
        _w = a[i][0]

print(c)
