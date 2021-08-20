from collections import defaultdict, deque
import heapq


class Solution:

    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        outgoing = defaultdict(dict)
        for (src, dest, n) in edges:
            outgoing[src][dest] = n
            outgoing[dest][src] = n
        traveled = defaultdict(dict)
        n_reached = 1
        visited = set([0])
        to_traverse = [(outgoing[0][dest], 0, dest) for dest in outgoing[0]]
        heapq.heapify(to_traverse)
        while len(to_traverse) > 0:
            (dist, src, dest) = heapq.heappop(to_traverse)
            inter = outgoing[src][dest]
            dist_at_node = dist - inter
            if dist_at_node < M:
                t = traveled.get(src, {}).get(dest, 0)
                try_dest = False
                if t == 0:
                    dist_edge = min(M - dist_at_node, inter)
                    if dist_edge == inter:
                        traveled[src][dest] = inter
                        traveled[dest][src] = inter
                        try_dest = M - dist_at_node - inter > 0
                    else:
                        traveled[src][dest] = dist_edge
                        traveled[dest][src] = -dist_edge
                    n_reached += dist_edge
                elif t < 0:
                    dist_edge = min(M - dist_at_node, inter + t)
                    traveled[src][dest] = dist_edge
                    n_reached += dist_edge
                if try_dest and dest not in visited:
                    n_reached += 1
                    visited.add(dest)
                    for (next_dest, next_inter) in outgoing[dest].items():
                        heapq.heappush(to_traverse, (dist_at_node + inter + 1 + next_inter, dest, next_dest))
        return n_reached
