mod = int(1e9+7)

for _ in range(int(input())):
 n, k = map(int, input().split())
 ans = (k ** n + k * ((-1) ** n)) // (k + 1)
 print(ans % mod)
