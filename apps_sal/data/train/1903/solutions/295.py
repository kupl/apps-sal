class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        costs = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                costs.append((cost, i, j))
        costs.sort(key=lambda x: x[0])
        group_label = [i for i in range(len(points))]
        result = 0
        combined = 0

        def find_group(target: int, group_label: List[int]) -> int:
            path = []
            while not target == group_label[target]:
                path.append(target)
                target = group_label[target]
            for node in path:
                group_label[node] = target
            return target

        def union_group(target: int, source: int, group_label: List[int]) -> int:
            while not source == group_label[source]:
                next_source = group_label[source]
                group_label[source] = target
                source = next_source
            group_label[source] = target
        while combined < len(points) - 1:
            (cost, target, source) = costs.pop(0)
            target_group = find_group(target, group_label)
            source_group = find_group(source, group_label)
            if not target_group == source_group:
                union_group(target_group, source, group_label)
                result += cost
                combined += 1
        return result
