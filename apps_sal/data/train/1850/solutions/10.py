from collections import defaultdict, deque

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        children = {}
        d = defaultdict(set)
        for edge in edges:
            d[edge[0]].add(edge[1])
            d[edge[1]].add(edge[0])
        visited = set()
        self.dist = 0
        def check(node, e):
            out = 1
            visited.add(node)
            for adj in d[node]:
                if adj not in visited:
                    out += check(adj, e + 1)
            children[node] = out
            self.dist += e
            return out
        
        check(0, 0)
        
        ans = [0] * N
        visited = {0}
        q = deque([(0, self.dist)])
        while len(q) > 0:
            cur, total = q.popleft()
            ans[cur] = total
            for adj in d[cur]:
                if adj not in visited:
                    q.append((adj, total + N - children[adj] - children[adj]))
                    visited.add(adj)
        return ans
            

