class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        conns = defaultdict(dict)
        for i, j, n in edges:
            conns[i][j] = n
            conns[j][i] = n

        heap = [(0, 0)]
        visited = set()
        ans = 0

        while heap:
            d, n = heapq.heappop(heap)
            if n not in visited:
                visited.add(n)
                ans += 1
                for m, inter in list(conns[n].items()):
                    if m in visited:
                        ans += min(M-d, conns[n][m])
                    else:
                        if d+inter < M:
                            heapq.heappush(heap, (d+inter+1, m))
                            ans += inter
                            conns[m][n] = 0
                        else:
                            ans += M-d
                            conns[m][n] -= M-d

        return ans

