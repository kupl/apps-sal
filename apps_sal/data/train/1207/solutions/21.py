for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    s = sum(l[1:])
    print(l[0] * s)
