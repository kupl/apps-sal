t = int(input())
for i in range(t):
    n, k, l = map(int, input().split())
    if k * l < n:
        print(-1)
    elif (k == 1 and n > 1):
        print(-1)
    else:
        for j in range(n):
            print((j % k) + 1, end=' ')
        print()
