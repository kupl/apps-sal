for t in range(int(input())):
    n = int(input())
    l = [int(k) for k in input().split()]
    m = [int(k) for k in input().split()]
    l.sort()
    m.sort()
    s = 0
    for j in range(n):
        s += min(l[j], m[j])
    print(s)
