def nck(n, k):
    if k > n or k < 0:
        return 0
    if k < n - k:
        k = n - k
    ans = 1.0
    for i in range(1, n - k + 1):
        ans = ans * (k + i) / i
    return ans


tc = int(input())
while tc:
    (s, n, m, k) = input().split()
    (s, n, m, k) = (int(s), int(n), int(m), int(k))
    prob = 0.0
    i = k
    while i < m:
        prob = prob + nck(m - 1, i) / nck(s - 1, n - 1) * nck(s - m, n - i - 1)
        i = i + 1
    print('{0:.6f}'.format(prob))
    tc = tc - 1
