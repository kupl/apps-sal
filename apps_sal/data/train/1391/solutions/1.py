from sys import stdin
input = stdin.readline
for i in range(int(input())):
    n, k = list(map(int, input().split()))
    l = []
    c = 0
    for g in range(n):
        adc = list(map(int, input().split()))
        l.append(adc)
    l.sort(key=lambda x: x[1])
    l.sort(key=lambda x: x[2])
    i = 0
    j = 0
    while i < n:
        if i != 0:
            if l[i][2] != l[i - 1][2]:
                c += 1
                j = i
            else:
                if (l[i][0]) >= (l[j][1]):
                    c += 1
                    j = i
        else:
            c += 1
        i += 1
    print(c)
