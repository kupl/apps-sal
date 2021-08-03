# cook your dish here
t = int(input())
while t > 0:
    n = int(input())
    l = [int(x) for x in input().split()]
    s = []
    s1 = 0
    for x in l:
        s1 = s1 + x
        s.append(s1)

    d = 0
    i = 0
    n = n - 1
    while n > 0:
        n = n - s[i]
        i = i + s[i]
        d = d + 1
    print(d)

    t = t - 1
