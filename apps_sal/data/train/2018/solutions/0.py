n, m = map(int, input().split())
a = list(map(int, input().split()))
p = 0
t = [0] * 3
for i in range(n):
    if(a[i] < a[p]):
        p = i
if(n == 2):
    print('0\n1 1\n')
else:
    a.sort()
    t[0] = min(a[0] + a[1] + m, a[1] + a[2])
    t[1] = max(a[0] + a[n - 1] + m, a[n - 2] + a[n - 1])
    t[2] = (a[n - 2] + a[n - 1]) - (a[0] + a[1])
    if(t[1] - t[0] > t[2]):
        p = n
    else:
        t[2] = t[1] - t[0]
    print(t[2])
    for i in range(n):
        print(int(i == p) + 1, end=' ')
