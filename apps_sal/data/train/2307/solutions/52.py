N, A, B = map(int, input().split())
X = [int(x) for x in input().split()]
score = 0
for i in range(N - 1):
    score += min((X[i + 1] - X[i]) * A, B)
print(score)
