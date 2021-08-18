try:
    t = int(input())
    a = []
    b = []
    for i in range(t):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    flag = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            a1 = a[i]
            b1 = b[i]
            a2 = a[j]
            b2 = b[j]
            if a1 + b1 == a2 and a2 + b2 == a1:
                flag = 1
    if flag == 1:
        print("YES")
    else:
        print("NO")
except Exception:
    pass
