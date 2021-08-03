n = int(input())
al = list(map(int, input().split()))
a_xor = al[0]
for i in range(1, n):
    a_xor ^= al[i]

ans = []
for a in al:
    ans.append(a_xor ^ a)

print(*ans)
