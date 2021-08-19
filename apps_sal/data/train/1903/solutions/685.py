import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst_nodes = [0 for i in range(n)]
        mst_nodes_cnt = 0
        h = []

        def man_dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        mst_nodes[0] = 1
        for p in range(1, n):
            h.append((man_dist(0, p), 0, p))
        heapq.heapify(h)
        tot_dist = 0
        while h:
            (dist, src_node, dst_node) = heapq.heappop(h)
            if mst_nodes[dst_node]:
                continue
            tot_dist += dist
            mst_nodes[dst_node] = 1
            mst_nodes_cnt += 1
            if mst_nodes_cnt == n:
                break
            for next_dst in range(n):
                if mst_nodes[next_dst] == 0:
                    heapq.heappush(h, (man_dist(dst_node, next_dst), dst_node, next_dst))
        return tot_dist
