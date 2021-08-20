3
(N, A, B) = (int(i) for i in input().split())
X = [int(x) for x in input().split()]
ret = 0
for i in range(1, N):
    d = X[i] - X[i - 1]
    if d * A <= B:
        ret += d * A
    else:
        ret += B
print(ret)
