T = int(input())
for t in range(T):
    N = int(input())
    S1 = input().split()
    S = list(range(N))
    for i in range(N):
        S[i] = int(S1[i])
    S.sort()
    diff = list(range(N - 1))
    for i in range(N - 1):
        diff[i] = abs(S[i] - S[i + 1])

    print(min(diff))
