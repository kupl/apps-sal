for _ in range(int(input())):
    n = int(input())
    ass = list(map(int, input().split()))
    m = 0
    for i in range(n):
        if ass.count(ass[i]) > m:
            m = ass.count(ass[i])
    print(n - m)
