# cook your dish here


t = int(input())

while t > 0:
    t -= 1
    n, s = list(map(int, (input()).split()))
    p = list(map(int, (input()).split()))
    a = list(map(int, (input()).split()))

    mind = 101
    minf = 101

    for j in range(n):
        if a[j] == 0:
            if p[j] < mind:
                mind = p[j]
        else:
            if p[j] < minf:
                minf = p[j]

    if mind + minf + s > 100:
        print("no")
    else:
        print("yes")
