n, l = map(int, input().split())
S = []

for i in range(n):
    s = input()
    S.append(s)

S.sort()

ans = ''
for i in range(n):
    ans += S[i]

print(ans)
