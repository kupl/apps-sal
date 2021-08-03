n = int(input())
a = list(map(int, input().split()))
tmp = 0
for x in a:
    tmp ^= x
ans = []
for i in range(n):
    ans.append(a[i] ^ tmp)
print(*ans)
