x, y = list(map(int, input().split()))
a = {}
for i in range(x):
    p, q = input().split()
    a[p] = q
for i in range(y):
    f = input().strip()
    if "." in f:
        print(a.get(f.split(".")[-1], "unknown"))
    else:
        print("unknown")
