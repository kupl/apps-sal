

t = int(input())
for _ in range(t):
    n = int(input())
    ans = (n * (n + 1) * (2 * n + 1))
    ans /= 6
    ans = int(ans)
    print(ans)
