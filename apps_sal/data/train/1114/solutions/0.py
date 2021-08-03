T = int(input())
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))[:N]
    l = []
    for j in range(len(A)):
        for k in range(j + 1, len(A)):
            l.append(A[j] + A[k])
    print(l.count(max(l)) / ((N * (N - 1)) / 2))
