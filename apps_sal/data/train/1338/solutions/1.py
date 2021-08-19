a = list(map(float, input().split()))
for i in range(int(a[0])):
    x, y = a[i * 2 + 1], a[i * 2 + 2]
    s = x * (10**y)
    # s=str(s)
    s = round(s, 2)
    s = str(s)
    s += "0"
    ind = s.index(".")
    print(s[:ind + 3])
