from queue import PriorityQueue
from collections import defaultdict


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        e_dict = defaultdict(dict)
        for i, j, n in edges:
            e_dict[i][j] = e_dict[j][i] = n

        seen = {}
        pq = PriorityQueue()
        pq.put((-M, 0))

        while pq.qsize() > 0:
            remaining_moves, idx = pq.get()
            if idx not in seen:
                seen[idx] = -remaining_moves
                for j in e_dict[idx]:
                    j_remaining_moves = seen[idx] - e_dict[idx][j] - 1
                    if j_remaining_moves >= 0 and j not in seen:
                        pq.put((-j_remaining_moves, j))

        res = len(seen)
        for i, j, k in edges:
            res += min(seen.get(i, 0) + seen.get(j, 0), k)

        return res
