for _ in range(int(input())):
    n, k, l = map(int, input().split())
    if k * l < n or (k == 1 and n != 1):
        print(-1)
    else:
        i = 1
        for _ in range(n):
            print(i, end=' ')
            if i == k:
                i = 0
            i += 1
        print()
