T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    W = list(map(int, input().split()))

    W.sort()

    if K <= N // 2:
        Kv = [W[i] for i in range(K)]
    else:
        Kv = [W[N - i - 1] for i in range(K)]
    for i in Kv:
        W.remove(i)

    diff = sum(Kv) - sum(W)
    if diff < 0:
        diff *= -1

    print(diff)
