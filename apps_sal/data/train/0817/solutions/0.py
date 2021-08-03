for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    su = l[0]
    for i in range(1, n):
        su ^= l[i]
    print(su)
