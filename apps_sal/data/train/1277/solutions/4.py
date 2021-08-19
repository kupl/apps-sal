# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    s = 0
    for j in range(n):
        p, q, d = map(int, input().split())
        tmp = p
        p = p + ((d / 100) * p)
        p = p - ((d / 100) * p)
        s = s + ((tmp - p) * q)
    print(s)
