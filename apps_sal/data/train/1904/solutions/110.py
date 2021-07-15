import operator
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        dict_m = {}
        for i in range(len(points)):
            pt = points[i]
            tmp = (pt[0] ** 2 + pt[1] ** 2)
            dict_m[i] = tmp
        sorted_m = sorted(list(dict_m.items()), key = operator.itemgetter(1))
        tmp = [t[0] for t in sorted_m]
        res = [points[tmp[i]] for i in range(K)]
        print(res)
        return res 
        # sorted_m.keys()
        # return res
        # res = sorted(res)
        # print(res)
        # return res[:K]

