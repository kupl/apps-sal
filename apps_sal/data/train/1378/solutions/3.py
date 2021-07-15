# cook your dish here
A, N, K = map(int, input().split())

ans = "" + str(A % (N + 1))
p = A // (N + 1)

for i in range(K - 1):
 ans += " " + str(p % (N + 1))
 p = p // (N + 1)

print(ans)
