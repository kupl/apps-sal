import sys
input = sys.stdin.readline
s = list(map(int, list(input())[: -1]))
if s[0] == 0 or s[-1] == 1:
    print(-1)
    return
n = len(s)
for i in range(n - 1):
    if s[i] != s[-2 - i]:
        print(-1)
        return
res = []
temp = []
s[-1] = 1
for i in range(n):
    if s[i] == 0 or i == 0:
        temp.append(i + 1)
    else:
        if len(res):
            p = res[-1][0]
            res.append((i + 1, p))
        if len(temp):
            while len(temp):
                res.append((i + 1, temp.pop()))
for _ in range(len(res)):
    print(*res.pop())
