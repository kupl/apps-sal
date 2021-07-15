class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        res = [-1] * n
        dry = []
        rained = {}
        for i, r in enumerate(rains):
            if r:
                if r not in rained:
                    rained[r] = i
                else:
                    if not dry:
                        return []
                    else:
                        idx = bisect.bisect_left(dry, rained[r])
                        if idx == len(dry):
                            return []
                        res[dry[idx]] = r
                        dry.pop(idx)
                        rained[r] = i
                        
            else:
                dry.append(i)
        for i in dry:
            res[i] = 1
        return res
