# cook your dish here
t = int(input())
for _ in range(t):
    x, r = map(int, input().split())
    i = 2
    l = []
    l1 = []
    while i <= x:
        if (x % i == 0):
            l.append(i)
        i = i + 1
    i = 2
    while i <= r:
        if (r % i == 0):
            l1.append(i)
        i = i + 1
    su = 0
    for i in range(len(l)):
        su += pow(l[i], r)
    # print(su)

    su1 = 0
    for i in range(len(l1)):
        su1 += l1[i] * x
    print(su, su1, sep=' ')
