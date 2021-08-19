try:
    # cook your dish here
    t = int(input())
    for j in range(t):
        n = int(input())
        x = []
        p = []
        m = []
        for i in range(n):
            X, P, M = list(map(str, input().split()))
            x.append(X)
            p.append(int(P))
            m.append(int(M))
            avg = sum(m) / n
        for i in m:
            if i < avg:
                z = sorted([k for k in m if k < avg])
                for i in range(len(z)):
                    print(x[m.index(z[i])], p[m.index(z[i])], m[m.index(z[i])])

except:
    pass
