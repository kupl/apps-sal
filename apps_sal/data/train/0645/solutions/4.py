def Test():
    n = int(input())
    k = int(input())
    low = min(k % n, n - k % n)
    print(min(n - 1, low * 2))


T = int(input())
for t in range(T):
    Test()
