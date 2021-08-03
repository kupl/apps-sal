# cook your dish here
for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            B.append(A[i] + A[j])
    C = max(B)
    D = N * (N - 1) // 2
    count = B.count(C)
    print('%0.8f' % (count / D))
