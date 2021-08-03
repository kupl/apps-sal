# cook your dish here
T = int(input())
for i in range(T):
    n, d = input().split()
    d = int(d)
    a = []
    l = len(n)
    mn = d

    for j in range(l):
        a.append(int(n[j]))

    for k in range(l - 1, -1, -1):
        if(a[k] > mn):
            a.pop(k)
            a.append(d)
        mn = min(mn, a[k])

    print(*a, sep="", end="\n")
    T = T - 1
