from sys import stdin, setrecursionlimit
import threading
n = int(stdin.readline())
w = [int(x) for x in stdin.readline().split()]
graph = [{} for x in range(n)]
for road in range(n - 1):
    u, v, c = [int(x) for x in stdin.readline().split()]
    u -= 1
    v -= 1

    if v in graph[u]:
        graph[u][v] = min(graph[u][v], c)
    else:
        graph[u][v] = c

    if u in graph[v]:
        graph[v][u] = min(graph[v][u], c)
    else:
        graph[v][u] = c

gas = [{} for x in range(n)]
highs = [[0, 0] for x in range(n)]

path = [(0, 0)]

ind = 0

while ind < len(path):
    cur, par = path[ind]
    edges = graph[cur]
    for x in edges:
        if x != par:
            path.append((x, cur))
    ind += 1


def mostGas(node, parent):
    edges = graph[node]
    high = w[node]
    high2 = w[node]

    for x in edges:
        if x != parent:
            gas[node][x] = highs[x][0] + w[node] - edges[x]
            if gas[node][x] > high:
                high, high2 = gas[node][x], high
            elif gas[node][x] > high2:
                high2 = gas[node][x]
    highs[node] = [high, high2]
    return high


'''def fillIn(node,parent):
    edges = graph[node]
    high,high2 = highs[node]
    for x in edges:
        if x != parent:
            if gas[node][x] == high:
                gas[x][node] = high2 - edges[x]
            else:
                gas[x][node] = high - edges[x]
            if gas[x][node] > highs[x][0]:
                highs[x] = [gas[x][node], highs[x][0]]
            elif gas[x][node] > highs[x][1]:
                highs[x][1] = gas[x][node]
            fillIn(x,node)'''

for x, y in path[::-1]:
    mostGas(x, y)
# fillIn(0,0)

high = 0

for x in range(n):
    high = max(high, highs[x][0] + highs[x][1] - w[x])
print(high)
