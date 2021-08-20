for _ in range(int(input())):
    N = int(input())
    field = []
    for i in range(N):
        field.append(list(map(int, input())))
    print(N * (N + 1) // 2)
