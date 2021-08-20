t = int(input())
for i in range(t):
    n = int(input())
    x = {}
    p = {}
    m = []
    for j in range(n):
        (x1, p1, m1) = input().split()
        m.append(int(m1))
        x[int(m1)] = x1
        p[int(m1)] = p1
    su = sum(m)
    avg = su / n
    m.sort()
    for j in range(n):
        if m[j] < avg:
            print(x[m[j]], end=' ')
            print(p[m[j]], end=' ')
            print(m[j])
