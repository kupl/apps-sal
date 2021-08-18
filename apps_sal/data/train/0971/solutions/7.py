for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    l = []
    for i in a:
        l.append(a.count(i))
    print(n - a.count(a[l.index(max(l))]))
