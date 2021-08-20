n = int(input())
a = list(map(int, input().split()))
s = 0
for x in a:
    s ^= x
ans = []
for x in a:
    ans.append(s ^ x)
print(*ans)
