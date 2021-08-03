for _ in range(int(input())):
    n = int(input())
    a = [int(z) for z in input().split()]
    m = 0
    a1 = list(set(a))
    for i in range(len(a1)):
        if a.count(a1[i]) > m:
            m = a.count(a1[i])
    print(n - m)
