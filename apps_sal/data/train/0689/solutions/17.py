def check(a, b):
    for i in range(t):
        if a[i] + b[i] in a:
            idx = a.index(a[i] + b[i])
            if a[idx] + b[idx] == a[i]:
                print('YES')
                return
    print('NO')


t = int(input())
a = []
b = []
for _ in range(t):
    (x, y) = map(int, input().split())
    a.append(x)
    b.append(y)
check(a, b)
