class Solution:

    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        neigh = {}
        for e in edges:
            neigh[e[0]] = neigh.get(e[0], []) + [e[1]]
            neigh[e[1]] = neigh.get(e[1], []) + [e[0]]
        front = [1]
        steps = 0
        p = {i: 0 for i in range(1, n + 1)}
        p[1] = 1
        visited = set([1])
        for steps in range(t):
            q = {}
            for i in p:
                if p[i] != 0:
                    if i == 1 and len(neigh.get(i, [])) == 0:
                        q[i] = p[i]
                    elif len(neigh.get(i, [])) <= 1 and i != 1:
                        q[i] = p[i]
                    else:
                        if i == 1:
                            nn = len(neigh.get(i, []))
                        else:
                            nn = len(neigh.get(i, [])) - 1
                        for j in neigh.get(i, []):
                            if not j in visited:
                                q[j] = p[i] / nn
                                visited.add(j)
            p = {i: q.get(i, 0) for i in range(1, n + 1)}
        return p.get(target, 0)
