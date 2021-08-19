def printAp(a, d, l):
    print(' '.join([str(int(a + i * d)) for i in range(l)]))


t = int(input())
for i in range(t):
    n = int(input())
    lst = [int(x) for x in input().split(' ')]
    a = 0
    diff = 0
    if (lst[0] + lst[2]) / 2 == lst[1]:
        a = lst[0]
        diff = lst[1] - lst[0]
    elif (lst[1] + lst[3]) / 2 == lst[2]:
        diff = lst[2] - lst[1]
        a = lst[1] - diff
    else:
        a = lst[0]
        diff = (lst[3] - lst[0]) / 3
    printAp(a, diff, n)
