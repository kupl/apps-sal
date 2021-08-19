T = int(input())
for i in range(T):
    (X, N) = list(map(int, input().split()))
    a = N // X
    if N % X != 0:
        S = (2 * X + (a - 1) * X) * (a / 2)
    else:
        S = (2 * X + (a - 2) * X) * ((a - 1) / 2)
    print(int(S))
