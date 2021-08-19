3.4
(n, m) = list(map(int, input().split()))
arr = [[] for i in range(n)]
used = [0 for i in range(n)]
ans = 0


def dfs(vertex):
    used[vertex] = 1
    langs = arr[vertex]
    for lang in langs:
        for (ind, next_vertex) in enumerate(arr):
            if lang in next_vertex and used[ind] == 0:
                dfs(ind)


test = 0
for i in range(n):
    arr[i] = list(map(int, input().split()[1:]))
    if len(arr[i]) == 0:
        test += 1
for node in range(n):
    if used[node] == 0:
        dfs(node)
        ans += 1
print(ans - 1 + (1 if test == n else 0))
