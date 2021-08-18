for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()
    b = [int(i) for i in input().split()]
    b.sort()
    s = 0
    for i in range(n):
        s += min(a[i], b[i])
    print(s)
