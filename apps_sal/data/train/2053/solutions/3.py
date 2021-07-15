n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
if a[-1] > b[0]:
    print(-1)
    return

if a[-1] == b[0]:
    print(sum(b) + sum(a[:-1]) * m)
else:
    print(sum(b) + a[-1] + sum(a[:-1]) * m - a[-2])
