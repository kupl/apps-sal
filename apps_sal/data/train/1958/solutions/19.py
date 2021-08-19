class Solution:

    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        d = collections.defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
            if len(d[groupSizes[i]]) == groupSizes[i]:
                res.append(d[groupSizes[i]])
                d[groupSizes[i]] = []
        return res
