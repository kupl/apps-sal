class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_cost = 0
        msp = set()
        distances = self.compute_all_distances(points)
        groups = defaultdict(set)
        for i in range(len(points)):
            groups[i].add(i)
        # print(distances)
        while distances:
            # print(groups)
            next_min = heapq.heappop(distances)
            # print(f\"considering dist: {next_min}\")
            g1 = self.find_group(groups, next_min[1])
            g2 = self.find_group(groups, next_min[2])
            if g1 != g2:
                min_cost += next_min[0]
                groups[g1] = groups[g1] | groups[g2]
                del groups[g2]
        return min_cost

    def find_group(self, groups: dict, i: int) -> int:
        for group in groups:
            if i in groups[group]:
                return group
        return 0

    def compute_all_distances(self, points: List[List[int]]) -> List[int]:
        distances = list()
        for i in range(len(points) - 1):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                d = self.dist(p1, p2)
                distances.append((d, i, j))
        heapq.heapify(distances)
        return distances

    def dist(self, p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
