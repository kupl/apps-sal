(n, a, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    toho = a * (x[i] - x[i - 1])
    tele = b
    ans += min(toho, tele)
print(ans)
