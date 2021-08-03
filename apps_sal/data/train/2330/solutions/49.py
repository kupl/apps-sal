s = list(input())
if s[0] != '1' or s[-1] != '0':
    print(-1)
    return
l = 0
r = len(s) - 2

while l <= r:
    if s[l] != s[r]:
        print(-1)
        return
    l += 1
    r -= 1

oya = 1
ans = [[1, 2]]

for i in range(1, len(s) - 1):
    node = i + 2
    if s[i] == '0':
        s[len(s) - i - 1] = '?'
        ans.append([oya, node])
    elif s[i] == '1':
        ans.append([oya, node])
        oya = node
        s[len(s) - i - 1] = '?'

    else:
        ans.append([oya, node])


for i in ans:
    print(*i, sep=' ')
