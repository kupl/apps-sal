def hcfnaive(a, b):
    if b == 0:
        return a
    else:
        return hcfnaive(b, a % b)


for i in range(int(input())):
    (N, A, K) = map(int, input().split())
    s = 180 * (N - 2)
    d = hcfnaive(A * N * (N - 1) + (s - N * A) * 2 * (K - 1), N * (N - 1))
    print((A * N * (N - 1) + (s - N * A) * 2 * (K - 1)) // d, N * (N - 1) // d)
