N, A, B = map(int, input().split())
X = list(map(int, input().split()))
print(sum(min((X[i + 1] - X[i]) * A, B) for i in range(N - 1)))
