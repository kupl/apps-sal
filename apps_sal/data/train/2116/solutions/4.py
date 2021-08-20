m = int(input())
s = input()
ans = []
mark = [True for _ in range(len(s))]
z = 'a'
i = 0
while i <= len(s) - m:
    k = i
    for j in range(i, i + m):
        if s[j] <= s[k]:
            k = j
    ans.append(s[k])
    z = max(z, s[k])
    mark[k] = False
    i = k
    i += 1
for i in range(len(s)):
    if s[i] < z and mark[i]:
        ans.append(s[i])
print(''.join((str(i) for i in sorted(ans))))
