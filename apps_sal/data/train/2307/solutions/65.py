(N, A, B) = map(int, input().split())
X = list(map(int, input().split()))
prev = X[0]
answer = 0
for x in X:
    if A * (x - prev) < B:
        answer += A * (x - prev)
    else:
        answer += B
    prev = x
print(answer)
