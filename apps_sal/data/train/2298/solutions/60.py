def getlist():
    return list(map(int, input().split()))


N, T = getlist()
A = getlist()
m = A[0]
plus = -float("inf")
cost = 1
for i in range(1, N):
    if A[i] - m == plus:
        cost += 1
    elif A[i] - m > plus:
        plus = A[i] - m
        cost = 1
    else:
        pass
    m = min(m, A[i])

print(cost)
