A, N, K = map(int, input().split())

ans = "" + str(A % (N + 1))
previous = A // (N + 1)

for i in range(K - 1):
    ans += " " + str(previous % (N + 1))
    previous = previous // (N + 1)

print(ans)
