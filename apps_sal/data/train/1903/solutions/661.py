class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def hamin(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        dist_list = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist_list.append([hamin(points[i], points[j]), i, j])
        dist_list = sorted(dist_list, key=lambda x: x[0])
        group_set = set()
        group_set.add(0)
        answer = 0
        while True:
            i = 0
            while i < len(dist_list):
                [dis, x, y] = dist_list[i]
                if x in group_set and y in group_set:
                    dist_list.pop(i)
                    continue
                if x in group_set:
                    group_set.add(y)
                    answer += dis
                    break
                if y in group_set:
                    group_set.add(x)
                    answer += dis
                    break
                i += 1
            if len(group_set) == len(points):
                break
        return answer
