for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    while(len(a) != 1):
        t = a[-1]
        a.pop()
        l = a[-1]
        a.pop()
        a.append((t + l) / 2)
    print('%.6f' % a[0])
