T = int(input())
for i in range(T):
    N = int(input())
    S = []
    J = []
    c = 0
    for j in range(N):
        (a, b) = list(map(int, input().split()))
        S.append(a)
        J.append(b)
        if abs(J[j] - S[j] > 5):
            c += 1
    print(c)
