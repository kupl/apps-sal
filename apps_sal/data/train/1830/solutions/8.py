class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = {}
        dries = []
        res = [-1] * len(rains)
        for i, rain in enumerate(rains):
            if rain == 0:
                if lakes:
                    dries.append(i)
                else:
                    res[i] = 1
            elif rain in lakes:
                if len(dries) == 0:
                    return []
                idx = bisect_right(dries, lakes[rain])
                if idx == len(dries):
                    return []
                res[dries.pop(idx)] = rain
                lakes[rain] = i
            else:
                lakes[rain] = i
        for d in dries:
            if lakes:
                res[d] = lakes.popitem()[0]
            else:
                res[d] = 1
        return res
