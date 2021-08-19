class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        length = len(points)
        if length <= K:
            return points

        # key: distance to origin
        # value: list index in points
        distances: Dict[int, List[int]] = defaultdict(list)
        for i, li in enumerate(points):
            distance = (li[0] ** 2 + li[1] ** 2) ** 0.5
            distances[distance].append(i)

        order = OrderedDict(sorted(distances.items()))
        ans = []
        for i, (key, value) in enumerate(order.items()):
            for j in value:
                ans.append(points[j])
            if len(ans) >= K:
                break
        return ans[:K]
