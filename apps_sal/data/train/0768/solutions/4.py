from sys import setrecursionlimit
setrecursionlimit(999999)


def createTree(n, par):
    graph = [[] for i in range(n + 1)]
    for i in range(len(par)):
        graph[par[i]].append(i + 2)
    return graph


def recurse(graph, root):
    if len(graph[root]) == 0:
        return [1, 1]
    noNodes = 1
    root_sum = 0
    for i in range(len(graph[root])):
        temp = recurse(graph, graph[root][i])
        noNodes += temp[0]
        root_sum = max(root_sum, temp[1])
    return [noNodes, root_sum + noNodes]


for i in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    graph = createTree(n, arr)
    print(recurse(graph, 1)[1])
