t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))[:n]
    c = 0
    d = 0
    e = 0
    ma = 0
    index = 0
    for i in range(len(a)):
        j = i + 1
        for k in range(j, len(a)):
            if a[i] == a[k]:
                c = c + 1
                break
    if c == len(a) - 1:
        print(0)
    else:
        for i in range(len(a)):
            j = i + 1
            f = 1
            for k in range(j, len(a)):
                if a[i] == a[k]:
                    f = f + 1
            if f > ma:
                ma = f
                index = a[i]
        for i in [index]:
            for j in range(len(a)):
                if i != a[j]:
                    d = d + 1
        if d > 0:
            print(d)
        else:
            for i in range(1, len(a)):
                if a[0] != a[i]:
                    e = e + 1
            print(e)
