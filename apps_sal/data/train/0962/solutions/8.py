T = int(input())
for t in range(T):
    N = int(input())
    for i in range(N):
        sol = ''
        if (i + N) % 2 == 0:
            for j in range(N - i, 0, -1):
                sol += str(j)
            print(sol)
        else:
            for j in range(1, N - i + 1):
                sol += str(j)
            print(sol)
