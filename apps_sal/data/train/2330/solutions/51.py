s = input()
N = len(s)
flag = True
if s[N - 1] == '1':
    flag = False
if s[0] == '0' or s[N - 2] == '0':
    flag = False
for i in range(N // 2):
    if s[i] != s[N - i - 2]:
        flag = False
        break
if flag:
    ans = []
    prev = 0
    for i in range(N // 2):
        if s[i] == '1':
            for j in range(prev, i):
                ans.append([i + 1, j + 1])
            prev = i
    for i in range(prev, N - 1):
        ans.append([N, i + 1])
    for a in ans:
        print(*a)
else:
    print(-1)
