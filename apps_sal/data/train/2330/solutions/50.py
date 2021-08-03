import sys
s = list(map(int, input()))
n = len(s)
if s[0] == 0 or s[-1] == 1:
    print((-1))
    return
for i in range(n):
    if s[i] != s[n - i - 2]:
        print((-1))
        return

cur_children = [0]
ans = []
for i in range(1, n - 1):
    if s[i] == 1:
        while len(cur_children) > 0:
            j = cur_children.pop()
            ans.append((i + 1, j + 1))
    cur_children.append(i)
while len(cur_children) > 0:
    j = cur_children.pop()
    ans.append((n, j + 1))
for i, j in ans:
    print((i, j))
