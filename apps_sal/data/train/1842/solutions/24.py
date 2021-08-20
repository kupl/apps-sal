class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        visited = [False for i in range(n + 1)]
        visited[0] = True
        visited[n] = True
        prb = [0 for i in range(n)]
        prb[0] = 1
        edgelists = [[] for i in range(n)]
        for i in edges:
            x = i[0] - 1
            y = i[1] - 1
            edgelists[x].append(y)
            edgelists[y].append(x)
        edgelists[0].append(n)
        curr = [0]
        for _ in range(t):
            nex = []
            print(curr)
            for i in curr:
                occ = False
                for j in edgelists[i]:
                    if visited[j] == False:
                        occ = True
                        nex.append(j)
                        prb[j] = prb[i] / (len(edgelists[i]) - 1)
                        visited[j] = True
                if occ:
                    prb[i] = 0
            curr = nex
        print(prb)
        return prb[target - 1]
