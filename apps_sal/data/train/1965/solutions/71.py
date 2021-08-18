from typing import List
from collections import defaultdict


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        AlicePath = defaultdict(set)
        BobPath = defaultdict(set)
        CommonPath = defaultdict(set)
        for type, u, v in edges:
            if type == 1 or type == 3:
                AlicePath[u - 1].add(v - 1)
                AlicePath[v - 1].add(u - 1)
            if type == 2 or type == 3:
                BobPath[u - 1].add(v - 1)
                BobPath[v - 1].add(u - 1)
            if type == 3:
                CommonPath[u - 1].add(v - 1)
                CommonPath[v - 1].add(u - 1)

        def count(m: defaultdict(set)):
            visited = [False] * n
            ret = 0

            def dfs(i: int, isNewGraph: bool):
                nonlocal ret
                if visited[i]:
                    return
                visited[i] = True
                if isNewGraph:
                    ret += 1
                for endPoint in m[i]:
                    dfs(endPoint, False)

            for i in range(n):
                dfs(i, True)

            return ret

        if count(AlicePath) > 1 or count(BobPath) > 1:
            return -1

        x = count(CommonPath)
        return len(edges) - (n + x - 2)
