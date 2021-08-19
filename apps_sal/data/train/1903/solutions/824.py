import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_nodes = set()  # int
        # mst_edges = set() # (int,int)
        h = []  # heap of edges connected to MST (distance, source, dest)
        def man_dist(i, j): return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        mst_nodes.add(0)
        for p in range(1, n):
            h.append((man_dist(0, p), 0, p))
        heapq.heapify(h)

        tot_dist = 0
        while h:
            dist, src_node, dst_node = heapq.heappop(h)
            if dst_node in mst_nodes:
                continue
            tot_dist += dist
            mst_nodes.add(dst_node)
            for next_dst in range(n):
                if next_dst not in mst_nodes:
                    heapq.heappush(h, ((man_dist(dst_node, next_dst), dst_node, next_dst)))
            pass

        return tot_dist
