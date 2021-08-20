class Solution:

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        edges_dict = collections.defaultdict(list)
        for (src, dest, weight) in edges:
            edges_dict[src].append((dest, weight))
            edges_dict[dest].append((src, weight))
        import heapq

        def get_reachable_count(nd, distance):
            heap = [(0, nd)]
            count = 0
            visited = set()
            while heap:
                (travelled, nd) = heapq.heappop(heap)
                if nd in visited:
                    continue
                visited.add(nd)
                count += 1
                for (dest, new_dist) in edges_dict[nd]:
                    if new_dist + travelled > distance or dest in visited:
                        continue
                    heapq.heappush(heap, (new_dist + travelled, dest))
            return count - 1
        get_reachable_count(1, distanceThreshold)
        curr_min_val = float('inf')
        curr_best_idx = -1
        for i in range(n):
            count = get_reachable_count(i, distanceThreshold)
            if count <= curr_min_val:
                (curr_min_val, curr_best_idx) = (count, i)
        return curr_best_idx
