# Pattern E
T = int(input())

for t in range(T):
    N = int(input())

    for i in range(N):
        sol = ""
        for j in range(1, N + 1):
            if((j + i) % N == 0):
                sol += str(N)
            else:
                sol += str((j + i) % N)
        print(sol)
