import sys

sys.setrecursionlimit(1000000)


def dfs(root, graph):
    retrieval = []
    try:
        for i in graph[root]:
            retrieval.append(dfs(i, graph))
        if(retrieval != []):
            mx = retrieval[0][0] + retrieval[0][1]
            totalNodesInSubtree = 0
            for i in retrieval:
                totalNodesInSubtree += i[1]
                if(i[0] + i[1] > mx):
                    mx = i[0] + i[1]
            return [mx, totalNodesInSubtree + 1]
        else:
            return[0, 1]
    except:
        return [0, 1]


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    graph = {}
    for i in range(n - 1):
        if(graph.get(l[i])):
            graph[l[i]].add(i + 2)
        else:
            graph[l[i]] = set([i + 2])
    ans = dfs(1, graph)
    print(ans[0] + ans[1])
