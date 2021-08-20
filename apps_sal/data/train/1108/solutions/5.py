(N, M, K) = map(int, input().split())
c = 0
for i in range(K):
    T = list(map(int, input().split()))[:K + 1]
    Q = T[-1]
    T.remove(T[-1])
    if Q <= 10:
        if sum(T) >= M:
            c += 1
print(c)
