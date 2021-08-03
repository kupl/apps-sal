n = int(input())
a = list(map(int, input().split()))
wa = a[0] ^ a[1]
for i in range(2, n):
    wa = wa ^ a[i]
ans = []
for i in range(n):
    ans.append(wa ^ a[i])
print(*ans)
