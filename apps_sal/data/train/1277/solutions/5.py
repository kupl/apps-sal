# cook your dish here
for i in range(int(input())):
    m = int(input())
    a = 0
    for j in range(0, m):
        p, q, d = list(map(int, input().split()))
        a += (p - ((p + (d * p) / 100) - (p + (d * p) / 100) * (d / 100))) * q
    print("{0:.9f}".format(a))
