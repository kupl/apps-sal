class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        smap = {}
        for i, s in enumerate(groupSizes):
            if s in smap:
                smap[s].append(i)
            else:
                smap[s] = [i]

        res = []
        for k, v in list(smap.items()):
            for i in range(0, len(v), k):
                res.append(v[i:i + k])
                p = i
        return res
