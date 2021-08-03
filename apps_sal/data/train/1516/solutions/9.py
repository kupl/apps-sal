t = int(input())
for i in range(t):
    [n, k] = input().split()
    n = int(n)
    k = int(k)
    a = k - 1
    d = 1 - n
    x = (a // (n - 1)) + 1
    ans = ((x * (2 * a + (x - 1) * d)) // 2) % 1000000007
    print(ans)
