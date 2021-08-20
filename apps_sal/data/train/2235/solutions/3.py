import sys
import threading
sys.setrecursionlimit(2100000)


def main():

    def counter(graph, vert, memo, pard=None):
        d = 0
        for c in graph[vert]:
            if c != pard:
                if len(graph[c]) == 1:
                    memo[c] = 0
                else:
                    memo[c] = counter(graph, c, memo, vert)[0]
                d += memo[c] + 1
        return (d, memo)
    n = int(input())
    vizinhos = []
    for _ in range(n):
        vizinhos.append([])
    for _ in range(n - 1):
        (i, j) = map(int, input().split())
        vizinhos[i - 1].append(j - 1)
        vizinhos[j - 1].append(i - 1)
    same = 1
    layer = [0]
    par = [None]
    j = 0
    while layer:
        j += 1
        n_layer = []
        n_pars = []
        for i in range(len(layer)):
            for vert in vizinhos[layer[i]]:
                if vert != par[i]:
                    n_layer.append(vert)
                    n_pars.append(layer[i])
        layer = n_layer
        par = n_pars
        if j % 2 == 0:
            same += len(layer)
    bipartite = same * (n - same)
    info = counter(vizinhos, 0, [None] * n)[1]
    dist = 0
    for g in info:
        if g != None:
            dist += (g + 1) * (n - g - 1)
    print((dist + bipartite) // 2)


threading.stack_size(140000000)
main_thread = threading.Thread(target=main)
main_thread.start()
main_thread.join()
