t = int(input())
for _ in range(t):
    n = int(input())
    n -= 1
    j = n * (n + 1) * (2 * n + 1) / 6
    print(int(j))
