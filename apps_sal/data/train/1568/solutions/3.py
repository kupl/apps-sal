for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in a:
        if i >= n // 2:
            c += 1
    print(c)
