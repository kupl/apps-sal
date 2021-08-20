import copy


class Solution:

    def findParent(self, v, parent):
        if parent[v] == -1:
            return v
        else:
            return self.findParent(parent[v], parent)

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        bothEdges = []
        aEdges = []
        bEdges = []
        aNodes = set()
        bNodes = set()
        for e in edges:
            if e[0] == 3:
                bothEdges.append(e)
                aNodes.add(e[2])
                aNodes.add(e[1])
                bNodes.add(e[2])
                bNodes.add(e[1])
            elif e[0] == 1:
                aEdges.append(e)
                aNodes.add(e[2])
                aNodes.add(e[1])
            else:
                bEdges.append(e)
                bNodes.add(e[2])
                bNodes.add(e[1])
        if len(aNodes) < n or len(bNodes) < n:
            return -1
        parents = [-1 for _ in range(n + 1)]
        mstCommon = 0
        for e in bothEdges:
            (x, y) = (e[1], e[2])
            xp = self.findParent(x, parents)
            yp = self.findParent(y, parents)
            if xp == yp:
                continue
            else:
                parents[xp] = yp
                mstCommon += 1
                if mstCommon == n - 1:
                    break
        if mstCommon == n - 1:
            return len(edges) - (n - 1)
        else:
            return len(edges) - (n - 1) - (n - 1) + mstCommon
