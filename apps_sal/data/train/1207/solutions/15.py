for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    s = 0
    for i in range(1, n):
        s += ls[i] * ls[0]
    print(s)
