import bisect

alphabetlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

A = input()
N = len(A)

dic = {moji: [] for moji in alphabetlist}
dp = [0 for i in range(N)]
check = set([A[-1]])
dic[A[-1]].append(N - 1)
for i in range(N - 2, -1, -1):
    check.add(A[i])
    dic[A[i]].append(i)
    if len(check) == 26:
        dp[i] = dp[i + 1] + 1
        check = set([])
    else:
        dp[i] = dp[i + 1]

for moji in alphabetlist:
    dic[moji].sort()

L = dp[0] + 1
ans = []
pos = -1
flag = 0

for i in range(L - 1):
    if flag == 1:
        break
    for moji in alphabetlist:
        if dic[moji]:
            index = bisect.bisect_left(dic[moji], pos)
            npos = dic[moji][index]
            if npos + 1 < N and dp[npos + 1] < L - (i + 1):
                pos = npos + 1
                ans.append(moji)
                break
            elif npos == N - 1:
                pos = N
                ans.append(moji)
                flag = 1
                break

if pos == N:
    ans.append("a")
    print("".join(ans))
else:
    s = set([])
    for i in range(pos, N):
        s.add(A[i])
    for moji in alphabetlist:
        if moji not in s:
            ans.append(moji)
            break
    print("".join(ans))
