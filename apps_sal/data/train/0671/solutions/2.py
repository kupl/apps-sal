# cook your dish here
for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    p = []
    q = []
    c = d = 0
    for i in range(n):
        if(b[i] == 0):
            c = 1
            p.append(a[i])
        else:
            d = 1
            q.append(a[i])
    if(c == 1):
        x = min(p)

    if(d == 1):
        y = min(q)

    s = 100 - s

    if(c == 0 or d == 0):
        print("no")
    elif((x + y) <= s):
        print("yes")
    else:
        print("no")
