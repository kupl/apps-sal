n = int(input())
a = list(map(int, input().split()))

uv = [[] for _ in range(n)]
for _ in range(n-1):
    i, j = map(int, input().split())
    uv[i-1].append(j-1)
    uv[j-1].append(i-1)

# DFS
# 頂点iが未探索の時、ans[i] = -1
ans = [-1 for _ in range(n)]
ans[0] = 1
# dp[i] = 長さi+1のLISの最後尾の最小値
dp = [a[0]]
# history[(i, j)]のとき、変更前はdp[i] = j
# stackとして使用
history = []
# 頂点parents[i] = iの親
parents = [-1 for _ in range(n)]

todo = []
for i in uv[0]:
    todo.append(i)
    parents[i] = 0

while True:
    i = todo.pop(-1)
    
    # ans[i]を求める
    if dp[-1] < a[i]:
        dp.append(a[i])
        history.append((-1, 0))
    else:
        # dpの変更点を二分探索
        start = 0
        stop = len(dp) - 1
        flag = True
        while start < stop:
            center = (start + stop) // 2
            if dp[center] < a[i]:
                start = center + 1
            elif dp[center] > a[i]:
                stop = center
            else:
                flag = False
                break
        if flag and dp[start] > a[i]:
            history.append((start, dp[start]))
            dp[start] = a[i]
        else:
            history.append((-2, 0))
    ans[i] = len(dp)

    # todoに追加
    for j in uv[i]:
        if ans[j] == -1:
            todo.append(j)
            parents[j] = i

    if len(todo) == 0:
        break

    # back
    j = i
    while parents[todo[-1]] != j:
        k = history.pop(-1)
        if k[0] == -2:
            None
        elif k[0] == -1:
            dp.pop(-1)
        else:
            dp[k[0]] = k[1]
        j = parents[j]

for i in ans:
    print(i)
