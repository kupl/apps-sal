for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    W = list(map(int, input().split()))
    W_cp = W.copy()
    count = 1
    curr = 0
    for (i, w) in enumerate(W):
        if w > k:
            count = -1
            break
        curr += w
        if curr > k:
            curr = w
            count += 1
    print(count)
