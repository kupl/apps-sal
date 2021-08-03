for i in range(int(input())):
    n, k = list(map(int, input().split()))
    q = [int(z) for z in input().split()]
    count = n - 1
    for i in range(n - 1):
        if q[i] > k:
            q[i + 1] += q[i] - k
    if q[n - 1] <= k:
        count += 1
    else:
        count += (q[n - 1] // k) + 1
    print(count)
