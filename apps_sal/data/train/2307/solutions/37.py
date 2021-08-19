(N, A, B) = list(map(int, input().split()))
X = list(map(int, input().split()))
c = 0
for i in range(N - 1):
    dist = X[i + 1] - X[i]
    if dist * A > B:
        c += B
    else:
        c += dist * A
print(c)
