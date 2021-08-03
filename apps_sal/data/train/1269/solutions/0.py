for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    s = 0
    for i in range(n):
        s += min(a[i], b[i])
    print(s)
