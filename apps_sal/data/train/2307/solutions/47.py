N, A, B = map(int, input().split())
L = list(map(int, input().split()))

count = 0

for i in range(1, N):
    p = L[i] - L[i - 1]
    if A * p >= B:
        count += B
    else:
        count += A * p

print(count)
