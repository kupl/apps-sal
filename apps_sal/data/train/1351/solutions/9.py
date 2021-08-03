for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = list(set(l))
    m.sort()
    k = []
    for i in range(n):
        if i in m:
            k.append(i)
        else:
            k.append(0)
    print(*k)
