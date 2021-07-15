import sys
sys.setrecursionlimit(int(1e6))
def solve(graph, cur):
    if not graph[cur]:
        return (1, 1)
    tot = 0
    ans = 0
    for child in graph[cur]:
        prevans, tnodes = solve(graph, child)
        tot += tnodes
        ans = max(ans, prevans)
    return tot + 1 + ans, tot + 1

for t in range(int(input())):
    n = int(input())
    lis = list(map(int, input(). split()))
    from collections import defaultdict
    graph = defaultdict(list)
    for i in range(n - 1):
        graph[lis[i]].append(i + 2)
    print(solve(graph, 1)[0])
