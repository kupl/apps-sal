n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
if a[-1] > b[0]:
    print(-1)
elif a[-1] == b[0]:
    print(sum(b) + sum(a[:-1]) * m)
else:
    print(sum(b) + a[-1] + sum(a[:-1]) * m - a[-2])
