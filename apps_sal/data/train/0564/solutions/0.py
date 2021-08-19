for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    c = list(map(int, input().split()))
    count = 1
    for i in range(n):
        if i + 1 < n:
            if c[i] - c[i + 1] >= k or c[i + 1] - c[i] >= k:
                continue
            else:
                count += 1
                (c[i], c[i + 1]) = (c[i + 1], c[i])
    print(count)
