class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        lakesFull = {}
        n = len(rains)
        dry = []
        res = []
        for i in range(n):
            l = rains[i]
            if l == 0:
                dry.append(i)
                res.append(-10000000)
                continue
            else:
                if l in lakesFull:
                    if len(dry) > 0:
                        di = -1
                        for dd in range(len(dry)):
                            if dry[dd] > lakesFull[l]:
                                di = dry[dd]
                                dry.pop(dd)
                                break
                        if di >= 0:
                            res[di] = l
                            del lakesFull[l]
                        else:
                            return []
                    else:
                        return []
                lakesFull[l] = i
                res.append(-1)
        for i in range(n):
            if res[i] == -10000000:
                res[i] = 1
        return res
