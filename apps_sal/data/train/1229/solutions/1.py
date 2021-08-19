T = int(input())
for _ in range(T):
    n, k = list(map(int, input().split()))
    seq = list(map(int, input().split()))
    motu, tomu = [], []
    for i in range(n):
        if i % 2 == 0:
            motu.append(seq[i])
        else:
            tomu.append((seq[i]))
    motu.sort(reverse=True)
    tomu.sort()
    for i in range(len(motu)):
        if len(tomu) - 1 < i:
            break
        if k == 0:
            break
        if tomu[i] < motu[i]:
            tomu[i], motu[i] = motu[i], tomu[i]
            k -= 1
    # for i in range(k):
    #     if motu[i] > tomu[i]:
    #         motu[i], tomu[i] = tomu[i], motu[i]
    if sum(tomu) > sum(motu):
        print("YES")
    else:
        print("NO")
