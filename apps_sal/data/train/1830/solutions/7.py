class Solution:

    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakes = {}
        dries = []
        res = []
        for (i, rain) in enumerate(rains):
            if rain == 0:
                dries.append(i)
                res.append(1)
            else:
                if rain in lakes:
                    if len(dries) == 0:
                        return []
                    idx = bisect_left(dries, lakes[rain])
                    if idx == len(dries):
                        return []
                    res[dries.pop(idx)] = rain
                lakes[rain] = i
                res.append(-1)
        return res
