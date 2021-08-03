T = int(input())

for t in range(T):
    N = int(input())

    for i in range(N):
        sol = "1"
        for j in range(2, N + 1):
            sol += str(i + 1) + str(j)
        print(sol + str(i + 1))
