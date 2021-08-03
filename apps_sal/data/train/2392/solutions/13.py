q = int(input())
for test in range(q):
    n, m = input().split()
    n = int(n)
    m = int(m)
    sumoften = 0
    for j in range(1, 10):
        sumoften += (m * j) % 10
    div = n // m
    ans = sumoften * (div // 10)
    for j in range(1, (div % 10) + 1):
        ans += (m * j) % 10
    print(ans)
