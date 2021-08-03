for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    c = 0
    if l.count(1) == n:
        print(0)
    else:
        for i in range(n):
            if l[i] == 0:
                c += (n - i) * 100
                break
        t = c + l.count(0) * 1000
        print(t)
