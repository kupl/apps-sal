for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    k = int(input())
    a = l[k - 1]
    l.sort()
    print(l.index(a) + 1)
