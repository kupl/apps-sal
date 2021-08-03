from heapq import *


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 0
        edge_list = []
        for idx1, [x1, y1] in enumerate(points):
            for idx2, [x2, y2] in enumerate(points[idx1 + 1:], idx1 + 1):
                heappush(edge_list, [abs(x1 - x2) + abs(y1 - y2), idx1, idx2])

        cost, p1, p2 = heappop(edge_list)
        add_point = {p1, p2}
        ret = cost
        while len(add_point) != len(points) and edge_list:
            temp_list = []
            flag = False
            while not flag:
                cost, p1, p2 = heappop(edge_list)
                if p1 in add_point and p2 in add_point:
                    continue
                elif p1 not in add_point and p2 not in add_point:
                    temp_list.append([cost, p1, p2])
                else:
                    add_point.add(p1)
                    add_point.add(p2)
                    ret += cost
                    flag = True
            while temp_list:
                heappush(edge_list, heappop(temp_list))

        return ret
