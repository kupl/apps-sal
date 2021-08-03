N = int(input())
for i in range(0, N):
    a = int(input())
    l = []
    n = (input())
    l = n.split()
    for x in range(0, len(l)):
        l[x] = int(l[x])
    l.sort()
    min = 1000000000
    for x in range(1, len(l)):
        s = int(l[x]) - int(l[x - 1])
        if min > (abs(s)):
            min = s
    print((str(min)))
