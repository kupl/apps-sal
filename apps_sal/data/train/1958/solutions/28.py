class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        res = []
        for i in range(len(groupSizes)):
            d[groupSizes[i]] = d.setdefault(groupSizes[i], []) + [i]
        for (x, y) in d.items():
            for j in range(0, len(y), x):
                res.append(y[j:j + x])
        return res
