from bisect import bisect_left

INF = 10 ** 9

N = int(input())
As = list(map(int, input().split()))

adj = [[] for _ in range(N)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    adj[u - 1].append(v - 1)
    adj[v - 1].append(u - 1)

ans = [0] * N
LIS = [INF] * (N + 1)
rewinder = []

parent = [-1] * N
stack = [0]
while stack:
    node = stack.pop()
    for next_node in adj[node]:
        if ans[next_node] == 0:
            parent[next_node] = node
            stack.append(next_node)

    while rewinder and rewinder[-1][0] != parent[node]:
        _, index, prev_value = rewinder.pop()
        LIS[index] = prev_value

    index = bisect_left(LIS, As[node])
    rewinder.append((node, index, LIS[index]))
    LIS[index] = As[node]

    ans[node] = bisect_left(LIS, INF)

print(*ans, sep='\n')
