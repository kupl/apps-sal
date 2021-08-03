for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    if l.count(1) == n:
        print(0)
    else:
        print(l.count(0) * 1000 + (n - l.index(0)) * 100)
