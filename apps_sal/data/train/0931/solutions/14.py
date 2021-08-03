for _ in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    c = 0
    for i in range(n):
        if b[i] % 2 == 0:
            c += b[i]
        else:
            continue
    print(c)
