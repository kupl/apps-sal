
for t in range(int(input())):
    n = int(input())
    k = int(input())
    low = min(k % n, n - k % n)
    print(min(n - 1, low * 2))
