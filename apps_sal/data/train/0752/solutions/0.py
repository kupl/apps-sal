n, m = list(map(int, input().split()))
a = {}
for i in range(n):
    x, y = input().split()
    a[x] = y
for i in range(m):
    c = input().strip()
    if '.' not in c:
        print("unknown")
    else:
        h = c.split('.')[-1]
        if h in a:
            print(a[h])
        else:
            print('unknown')
