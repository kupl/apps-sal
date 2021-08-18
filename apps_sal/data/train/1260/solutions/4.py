def dfs(i):
    visited[i] = True
    musuemsPossible = musuems[i]
    for j in neighbours[i]:
        if(not visited[j]):
            musuemsPossible += dfs(j)
    return musuemsPossible


t = int(input())
for _ in range(t):
    a = [int(x) for x in input().split()]
    n = a[0]
    m = a[1]
    k = a[2]
    neighbours = []
    visited = []
    for i in range(n + 1):
        visited.append(False)
        neighbours.append([])
    for i in range(m):
        a = [int(x) for x in input().split()]
        neighbours[a[0]].append(a[1])
        neighbours[a[1]].append(a[0])

    musuems = [0]
    m2 = [int(x) for x in input().split()]
    for i in m2:
        musuems.append(i)

    mususeumsBigNode = []
    for i in range(1, n + 1):
        if(not visited[i]):
            mususeumsBigNode.append(dfs(i))

    sorted(mususeumsBigNode)
    if len(mususeumsBigNode) < k:
        print(-1)
    else:
        mususeumsBigNode.sort()
        if k % 2 == 0:
            k //= 2
            ans = sum(mususeumsBigNode[:k] + mususeumsBigNode[-k:])
        else:
            k //= 2
            ans = mususeumsBigNode[-k - 1]
            if k > 0:
                ans += sum(mususeumsBigNode[:k] + mususeumsBigNode[-k:])
        print(ans)
