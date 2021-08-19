for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    p = []
    for i in range(n):
        p.insert(i - 1, 0)
    for i in set(l):
        p[i] = i
    for i in p:
        print(i, end=' ')
    print(end='\n')
