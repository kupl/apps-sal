import bisect

def dfs(graph, root, A, res, lis):
    stack = [(root,)]
    while stack:
        # print(stack)
        state = stack[-1]
        del stack[-1]
        u = state[0]
        if res[u] == -1:
            a = A[u]
            p = bisect.bisect_left(lis, a)
            if p == len(lis):
                stack.append((u, -1))
                lis.append(a)
            else:
                stack.append((u, p, lis[p]))
                lis[p] = a
            res[u] = len(lis)
            for v in graph[u]:
                if res[v] == -1:
                    stack.append((v,))
        else:
            p = state[1]
            if p >= 0:
                lis[p] = state[2]
            else:
                del lis[-1]

n = int(input())
A = [int(x) for x in input().split()]
graph = [[] for i in range(n)]
for i in range(n - 1):
    u, v = [int(x) - 1 for x in input().split()]
    graph[u].append(v)
    graph[v].append(u)
res = [-1] * n
dfs(graph, 0, A, res, [])
print(*res, sep='\n')
