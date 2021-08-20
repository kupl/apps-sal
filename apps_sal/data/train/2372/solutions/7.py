T = int(input())


def copy(N):
    Max = 1
    Min = n
    while Max * Max <= N:
        Min = min(Min, Max - 1 + N // Max - 1 + min(1, N % Max))
        Max += 1
    return Min


for i in range(T):
    n = int(input())
    print(copy(n))
