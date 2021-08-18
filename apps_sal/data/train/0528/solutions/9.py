try:
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().split()))
        if n == 1:
            print(m)
        elif n == 2:
            print((m // 2) - 1)
except EOFError as e:
    pass
