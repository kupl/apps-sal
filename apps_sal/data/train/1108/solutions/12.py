(N, M, K) = map(int, input().split())
cnt = 0
while N:
    (*T, Q) = map(int, input().split())
    if sum(T) >= M and Q < 11:
        cnt += 1
    N -= 1
print(cnt)
