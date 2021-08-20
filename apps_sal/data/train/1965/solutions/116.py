class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for (t, s, e) in edges:
            graph[s].append((-t, e))
            graph[e].append((-t, s))
        root = [1]
        candidates = []
        for (t, e) in graph[1]:
            heapq.heappush(candidates, (t, e))
        A = set(root)
        B = set(root)
        ans = 0
        while candidates:
            (t, e) = heapq.heappop(candidates)
            if -t == 1:
                if e in A:
                    continue
                A.add(e)
                ans += 1
                for (nt, ne) in graph[e]:
                    heapq.heappush(candidates, (nt, ne))
            elif -t == 2:
                if e in B:
                    continue
                B.add(e)
                ans += 1
                for (nt, ne) in graph[e]:
                    heapq.heappush(candidates, (nt, ne))
            else:
                if e in A and e in B:
                    continue
                A.add(e)
                B.add(e)
                ans += 1
                for (nt, ne) in graph[e]:
                    heapq.heappush(candidates, (nt, ne))
        if len(A) == n and len(B) == n:
            return len(edges) - ans
        return -1
