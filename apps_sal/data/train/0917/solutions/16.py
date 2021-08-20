for _ in range(int(input())):
    (N, K) = map(int, input().split())
    A = list(map(int, input().split()))
    m = abs(A[0] + A[1] - K)
    c = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            m = min(abs(A[i] + A[j] - K), m)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if abs(A[i] + A[j] - K) == m:
                c += 1
    print(m, c)
