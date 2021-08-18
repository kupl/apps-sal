t = int(input())
while(t > 0):
    n = int(input())
    ar = [int(i) for i in input().split()]
    while(len(ar) != 1):
        ar.sort(reverse=True)
        a = ar.pop(0)
        b = ar.pop(0)
        c = (a + b) / 2
        ar.append(c)
    a = ('%.6f' % ar[0])
    print(a)
    t = t - 1
