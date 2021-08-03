
import math
import bisect

n = int(input())
alist = [0] + list(map(int, input().split()))
uv_list = []
for i in range(n - 1):
    u, v = list(map(int, input().split()))
    if u > v:
        u, v = v, u
    uv_list.append([u, v])

tree = [[] for _ in range(n + 1)]
for i in range(n - 1):
    uv = uv_list[i]
    tree[uv[0]].append(uv[1])
    tree[uv[1]].append(uv[0])


queue = [1]
used = [0] * (n + 1)
ans = [0] * (n + 1)
dp = []
stack = []
while queue != []:
    cur = queue[-1]

    if used[cur] == 0:
        if cur == 1:
            dp.append(alist[cur])
            stack.append([len(dp) - 1, None])
        else:
            if alist[cur] > dp[-1]:
                dp.append(alist[cur])
                stack.append([len(dp) - 1, None])
            else:
                offset = bisect.bisect_left(dp, alist[cur])
                stack.append([offset, dp[offset]])
                dp[offset] = alist[cur]
        ans[cur] = len(dp)

    if tree[cur] != [] and used[cur] == 0:
        for child in tree[cur]:
            if used[child] == 0:
                queue.append(child)
    else:
        queue.pop()

        # reverse
        back = stack.pop()
        if back[1] == None:
            dp.pop()
        else:
            dp[back[0]] = back[1]
    used[cur] = 1
for i in range(n):
    print((ans[i + 1]))
