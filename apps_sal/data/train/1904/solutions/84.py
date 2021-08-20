from collections import defaultdict


class Solution:

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dic = defaultdict(list)
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2
            dic[distance].append(points[i])
        dis_list = sorted(dic.keys())
        ans = []
        for i in dis_list:
            ans.extend(dic[i])
        return ans[:K]
