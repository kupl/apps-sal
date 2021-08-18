class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, insert_cnt in edges:
            graph[u].append((v, insert_cnt))
            graph[v].append((u, insert_cnt))

        hq = [(-M, 0)]
        moves_left = collections.defaultdict(int)

        while len(hq) > 0:
            curr_moves_left, curr_node = heappop(hq)
            curr_moves_left = -curr_moves_left

            if curr_node in moves_left:
                continue
            moves_left[curr_node] = curr_moves_left

            for next_node, insert_cnt in graph[curr_node]:
                if insert_cnt >= curr_moves_left:
                    continue
                heappush(hq, (-(curr_moves_left - insert_cnt - 1), next_node))

        res = len(moves_left)
        for u, v, insert_cnt in edges:
            res += min(moves_left[u] + moves_left[v], insert_cnt)
        return res
