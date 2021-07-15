
from collections import defaultdict
import copy
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        def find(s, i):
            if s[i] != i:
                s[i] = find(s, s[i])
            return s[i]
        
        def union(s, i, j):
            if i > j:
                i, j = j, i
            s[find(s, j)] = s[find(s, i)]
        
        def is_connected(s, i, j):
            return find(s, i) == find(s, j)
        
        def is_full_connect(s):
            return all(is_connected(s, i, i+1) for i in range(len(s) - 1))

        
        d = defaultdict(set)
        res = 0
        uf = list([i for i in range(n)])
        for t, i, j in edges:
            d[t].add((i-1, j-1))
        for i, j in d[3]:
            if is_connected(uf, i, j):
                res += 1
            else:
                union(uf, i, j)
        uf1, uf2 = copy.copy(uf), copy.copy(uf)

        for i, j in d[1]:
            if is_connected(uf1, i, j):
                res += 1
            else:
                union(uf1, i, j)

        for i, j in d[2]:
            if is_connected(uf2, i, j):
                res += 1
            else:
                union(uf2, i, j)

        if not is_full_connect(uf1) or not is_full_connect(uf2):
            return -1

        return res

