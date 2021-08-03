for _ in range(int(input())):
    n = int(input())
    a = []
    b = []
    d = []
    for i in range(n):
        a.append(input())
        b.append(int(input()))
        c = b
    c = sorted(c)
    for i in range(n):
        for j in range(n):
            if(c[i] == b[j]):
                d.append(a[j])
    for i in d:
        print(i)
