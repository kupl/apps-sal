t = int(input())
for i in range(t):
    l, k = map(int, input().split())
    if k > l:
        x = 0
    else:
        x = ((l - k + 1) * (l - k + 2)) // 2
    print("Case ", i + 1, ": ", x, sep='')
